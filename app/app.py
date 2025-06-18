from fastapi import FastAPI, UploadFile, File
from app.tasks import summarize_document 

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = file(...)):
    content = await file.read()
    summarize_document.delay(file.filename, content.decode())
    return {"status": "uploaded"}