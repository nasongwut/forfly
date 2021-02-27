import os
import uvicorn
from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse



app = FastAPI()


@app.get('/')
def root():
    return {'message': 'forfly is running'}

@app.post('/member/{username}/{mission}')
async def readImg(username: str, mission: str):

    imgDict = {}
    userPath = './member/'+username+'/'+mission+'/images'
    imgFolder = ['person', 'vehicle', 'fire', 'smoke']
    for x in imgFolder:
        readIn = os.listdir(userPath+'/'+x)
        count = 1
        temp = {}
        for i in readIn:
            temp[count] = i
            count += 1
        count = 1
        imgDict[x] = temp
    return imgDict


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
