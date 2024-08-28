import logging, json, os.path
from fastapi import FastAPI
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from mangum import Mangum
from api import app as api_app
from pathlib import Path

#logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
handler = Mangum(app)
app.mount("/api", api_app, name='api')

"""
# Serve static files in an alternate method
# Doesn't require '.html' extension in url
@app.get("/{page_name}")
async def serve_page(page_name: str):
    file_path = os.path.join("static", f"{page_name}")
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    if os.path.isfile(file_path+'.html'):
        return FileResponse(file_path+'.html')"""

"""
@app.get("/{page_name}")
async def serve_page(page_name: str):
    file_path = Path("static") / f"{page_name}.html" if not page_name.endswith('.html') else Path("Static") / page_name
    if file_path.exists():
        return FileResponse(file_path)
    return Response('Page not found', 404)
"""

#app.mount("/", StaticFiles(directory='static', html=True), name='static')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)