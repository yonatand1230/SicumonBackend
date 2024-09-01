from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel
from typing import Annotated
from sicumon.sicum import Sicum
from sicumon.db import Db
from sicumon.utils import Utils

class FileItem(BaseModel):
    fileName: str
    subject: str
    uploaderName: str
    grade: int

app = FastAPI()

@app.get("/get_file_meta")
def handle_get_file_meta(fileKey: str):
    item = Db.get_file_meta(fileKey)
    return JSONResponse(item.__dict__)

@app.get("/get_file_list")
def handle_subject(subject: str, grade: int, Limit: int = 10, ExclusiveStartKey:str=None):
    if Limit>20: raise Exception('Limit too high!')
    items_json = []
    response = Db.get_files_by_subject(subject, grade, Limit=Limit, ExclusiveStartKey=ExclusiveStartKey)
    items = response.get('Items')
    for f in items: items_json.append(Utils.replace_decimals(f.__dict__))
    my_response = {
        'Items': items_json
    }
    if response.get('LastEvaluatedKey'): my_response['LastEvaluatedKey']=response.get('LastEvaluatedKey')
    return JSONResponse(my_response, headers={'Access-Control-Allow-Origin':'*'})

"""@app.post("/upload_file")
def upload_file(file_item: FileItem):
    file_meta = Sicum.from_dict(file_item.__dict__)
    print(file_meta.__dict__)
    Db.new_file()
"""

@app.post("/upload_file")
def upload_file(uploaded_file: Annotated[UploadFile, File()], uploader: Annotated[str, Form()], grade: Annotated[int, Form()], subject: Annotated[str, Form()]):
    file_meta = Sicum.from_dict({'uploaderName': uploader, 'grade': grade, 'subject': subject, 'fileName': uploaded_file.filename})
    print(file_meta.__dict__)
    uploaded = Db.new_file(file=uploaded_file.file, file_meta=file_meta)
    return JSONResponse(uploaded.__dict__, headers={'Access-Control-Allow-Origin':'*'})
    #return Response(status_code=204, content=None, headers={'server':'uvicon', 'Access-Control-Allow-Origin':'*'})