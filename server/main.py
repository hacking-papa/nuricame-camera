import shutil
from fastapi import FastAPI, UploadFile

from HED import convert

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def post_item(file: UploadFile):
    with open("input.jpg", "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
    convert("input.jpg")
    return {"filename": file.filename}
