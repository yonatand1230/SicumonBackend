import logging, json, os.path
from fastapi import FastAPI
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from mangum import Mangum
from api import app as api_app
from pathlib import Path

app = FastAPI()
app.mount("/api", api_app, name='api')
handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)