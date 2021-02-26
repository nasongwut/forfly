import os
import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def root():
    return {'message': 'forfly is running'}


@app.get('/file')
def file():
    imgList = os.listdir('img')
    imgDict = {}
    count = 0
    for i in imgList:
        imgDict[count] = i
        count += 1
    return imgDict


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000)
