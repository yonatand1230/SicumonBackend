import logging, json, os.path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from api import app as api_app

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
app.mount("/api", api_app, name='api')
app.mount("/", StaticFiles(directory='static', html=True), name='static')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)