from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def post_item(file: UploadFile):
    return {"filename": file.filename}
