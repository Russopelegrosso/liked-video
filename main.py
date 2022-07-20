import requests
import re
from fastapi import FastAPI
from pydantic import BaseModel
import os
app = FastAPI()


class UrlRequest(BaseModel):
    url: str


@app.post("/ifttt")
async def root(request: UrlRequest):
    # Download by youtube-dl
    path_to_folder = '/home/russo/Загрузки/'
    url = request.url
    os.system(f'youtube-dl -o {path_to_folder}"%(title)s.%(ext)s" {url}')
    print('ready============')

    # Download by requests
    # url = url.replace('www.youtube.com', 'www.youpak.com')
    # answer = requests.get(url)
    # content = answer.content
    # dwd_link = ''
    # pattern = r'<a href="(.+?)">'
    # for i in re.findall(pattern, str(content)):
    #     if 'p720' in i:
    #         dwd_link = i.split(' - Downloaded')[0]
    # requests.get(dwd_link)
    return ""
