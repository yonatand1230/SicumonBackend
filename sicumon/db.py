import boto3, io, os
from .sicum import Sicum
from dotenv import load_dotenv
from boto3.dynamodb.conditions import Attr
from datetime import datetime

# Init .env
load_dotenv() 

# Connect to AWS
session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='il-central-1'
)

# Connect to S3
resource = session.resource('s3', region_name='il-central-1')
s3 = resource.meta.client

# Connect to DynamoDB
dynamodb = session.resource('dynamodb', region_name='il-central-1')
table = dynamodb.Table('Files')

class Db:
    def new_file(file: io.BytesIO, file_meta: Sicum):
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
                'uploaderName': file_meta.uploaderName
            }
        )
        # Return updated file_meta 
        file_meta.fileKey = file_key
        return file_meta

    def generate_file_url(file_key: str):
        return s3.generate_presigned_url('get_object', Params={'Bucket':os.getenv('S3_ACCESS_POINT'),'Key':file_key})