import boto3, io, os
from dotenv import load_dotenv
from boto3.dynamodb.conditions import Attr

"""
from sicumon.db import Db
files=Db.get_files_by_subject('Math')
items=[]
for f in files:
    items.append(f.__dict__)

print(items)


"""
load_dotenv()

session = boto3.Session(
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key'),
    region_name='il-central-1'
)

#resource = session.resource('s3', region_name='il-central-1')
#s3 = resource.meta.client
#url = s3.generate_presigned_url('get_object', Params={'Bucket':S3_ACCESS_POINT,'Key':'files/enemy_test2.pdf'})
#print(url)

dynamodb = session.resource('dynamodb', region_name='il-central-1')
t = dynamodb.Table('Files')

response = t.scan(
    FilterExpression=Attr('subject').eq('Math'),
    Limit=2,
    ExclusiveStartKey=None
)
print(response)


#print(t.get_item(Key={'fileKey':'files/yom_hamea.pdf'}).get('Item'))


"""
res = t.put_item(
    Item={
        'fileKey': 'files/other_file.pdf',
        'fileName': 'other_file.pdf',
        'subject': 'Math',
        'uploadDate': 1234,
        'uploaderName': 'YonatanDaga'
    }
)
print(res)
#uploader_name='Yonatan51'
#response = t.scan(
#    FilterExpression=Attr('uploaderName').eq('Yonatan51'),
#)
#print(response)

#print(s3)
#b = open('/Users/yonatandaga/Documents/The Enemy - Yonatan Daga.pdf','rb').read()
#f = io.BytesIO(b)
#s3.upload_fileobj(f, 'sicumon', 'files/enemy_test2.pdf')
"""