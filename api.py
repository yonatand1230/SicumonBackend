from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sicumon.db import Db
from sicumon.utils import Utils

app = FastAPI()

@app.get("/get_file_meta")
def handle_get_file_meta(fileKey: str):
    item = Db.get_file_meta(fileKey)
    return JSONResponse(item.__dict__)

@app.get("/get_subject")
def handle_subject(subject: str, Limit: int = 10, ExclusiveStartKey:str=None):
    if Limit>20: raise Exception('Limit too high!')
    items_json = []
    response = Db.get_files_by_subject(subject, Limit=Limit, ExclusiveStartKey=ExclusiveStartKey)
    items = response.get('Items')
    for f in items: items_json.append(Utils.replace_decimals(f.__dict__))
    my_response = {
        'Items': items_json
    }
    if response.get('LastEvaluatedKey'): my_response['LastEvaluatedKey']=response.get('LastEvaluatedKey')
    return JSONResponse(my_response)