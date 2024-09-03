import boto3, io, os
from .sicum import Sicum
#from dotenv import load_dotenv
from boto3.dynamodb.conditions import Attr
from datetime import datetime
from .utils import Utils

AWS_KEYID = os.environ['AWS_KEYID']
AWS_SECRET = os.environ['AWS_SECRET']
AWS_REGION = 'il-central-1'
S3_ACCESSPOINT = os.environ['S3_ACCESSPOINT']

def file_size(file) -> int:
    # Get (temp) file size in bytes
    size = file.seek(0,2)
    file.seek(0)
    return size

def replace_decimals_list(list_to_replace):
    newlist = []
    for item in list_to_replace:
        newlist.append(Utils.replace_decimals(item))
    return newlist

def new_session():
    return boto3.Session(
        aws_access_key_id=AWS_KEYID,
        aws_secret_access_key=AWS_SECRET,
        region_name=AWS_REGION
    )

class Db:
    def new_file(file: io.BytesIO, file_meta: Sicum) -> Sicum:
        session = new_session() # Open AWS Session

        resource = session.resource('s3') # Connect to S3
        s3 = resource.meta.client

        dynamodb = session.resource('dynamodb') # Connect to DynamoDB
        table = dynamodb.Table('Files')
        
        
        file_meta.fileSize = file_size(file) # Get file size

        # Upload file to S3
        file_key = f'files/{file_meta.fileName}' 
        s3.upload_fileobj(file, 'sicumon', file_key)
        
        # Add meta to DynamoDB
        upload_date = datetime.now().strftime('%s')
        res = table.put_item(
            Item={
                'fileKey': file_key,
                'fileName': file_meta.fileName,
                'subject': file_meta.subject,
                'uploadDate': upload_date,
                'uploaderName': file_meta.uploaderName,
                'grade': file_meta.grade,
                'fileSize': file_meta.fileSize
            }
        )
        # Return updated file_meta 
        file_meta.fileKey = file_key
        file_meta.uploadDate = upload_date
        return file_meta

    def generate_file_url(file_key: str) -> str:
        resource = new_session().resource('s3') # Connect to S3
        s3 = resource.meta.client
        return s3.generate_presigned_url('get_object', Params={'Bucket':S3_ACCESSPOINT ,'Key':file_key})
    
    def get_file_meta(file_key: str) -> Sicum:
        dynamodb = new_session().resource('dynamodb') # Connect to DynamoDB
        table = dynamodb.Table('Files')

        response = table.get_item(Key={'fileKey': file_key})
        item = response.get('Item') # Get Item
        
        if not item: return None
        return Sicum.from_dict(item)
    
    """def get_files_by_subject(subject: str, grade: int, Limit: int = 10, ExclusiveStartKey:str=None, get_json=False) -> dict:
        dynamodb = new_session().resource('dynamodb') # Connect to DynamoDB
        table = dynamodb.Table('Files')
        response = None

        print('a')
        try:
            if ExclusiveStartKey:
                response = table.scan(
                    FilterExpression=Attr('subject').eq(subject)&Attr('grade').eq(grade),
                    Limit=Limit,
                    ExclusiveStartKey={'fileKey':ExclusiveStartKey}
                )
            else:
                response = table.scan(
                    FilterExpression=Attr('subject').eq(subject)&Attr('grade').eq(grade),
                    Limit=Limit
                )
            print(response)
        except Exception as e:
            print(e)
        
        if get_json: return response

        items_json = response.get('Items')
        items = []
        for i in items_json: items.append(Sicum.from_dict(i))
        print(items)
        
        my_response = {
            "Items": items
        }
        if response.get('LastEvaluatedKey'): my_response['LastEvaluatedKey']=response.get('LastEvaluatedKey').get('fileKey')
        
        return my_response"""
    
    def get_files_by_subject(subject: str, grade: int, Limit: int = 10, ExclusiveStartKey: str = None):
        dynamodb = new_session().resource('dynamodb') # Connect to DynamoDB
        table = dynamodb.Table('Files')
        response = {}

        if ExclusiveStartKey:
            response = table.scan(
                FilterExpression = Attr('subject').eq(subject) & Attr('grade').eq(grade),
                Limit = Limit,
                ExclusiveStartKey = {'fileKey': ExclusiveStartKey}
            )
        else: # api didnt get ExclusiveStartKey 
            response = table.scan(
                FilterExpression = Attr('subject').eq(subject) & Attr('grade').eq(grade),
                Limit = Limit
            )

        print(response)
        items = response.get('Items')
        items_fixed = replace_decimals_list(items)

        response_fixed = {
            'Items': items_fixed
        }

        # Response: Items, LastEvaluatedKey
        if response.get('LastEvaluatedKey'):
            print(response.get('LastEvaluatedKey'))
            lastKey = response.get('LastEvaluatedKey').get('fileKey')
            response_fixed['LastEvaluatedKey'] = lastKey
        
        print(response_fixed)