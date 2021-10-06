#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import requests
import random
import datetime
import dotenv
from dotenv import load_dotenv
load_dotenv()
def video_alert():
    telegram_chatID= os.getenv('chatID')
    telegram_token = os.getenv('API_TOKEN')
    telegram_baseurl = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    print(telegram_chatID)
    URL = f"https://www.googleapis.com/youtube/v3/search?part=snippet&key={os.getenv('youtubeAPI')}"
    param = {

        "type": "video",
        "channelId": "UCclfz6zVWWOpsQsg3OheI3g",
        "order": "date",
        "maxResults": 150,

    }

    resp = requests.get(url=URL, params= param)
    data = resp.json()
    newline = ord('\n')
    video_date= data["items"][0]["snippet"]["publishedAt"]
    format = '%Y-%m-%dT%H:%M:%SZ'
    datetime_str = datetime.datetime.strptime(video_date, format)

    video_title= ""
    id= ""
    if (datetime.datetime.now()-datetime_str).days<1:
        video_title= data['items'][0]['snippet']['title']
        id= data['items'][0]['id']['videoId']
    else:
        x = random.randint(0, len(data["items"]) - 1)
        video_title=data["items"][x]["snippet"]["title"]
        id= data['items'][x]['id']['videoId']
    youtube_url = f"https://www.youtube.com/watch?v={id}"
    message="Good Morning Sid!\nHere is today's Video: \n{} \n{}".format(video_title, youtube_url)

    telegram_params = {
        "chat_id": telegram_chatID,
        "text": message,
    }
    telegram_response = requests.get(url=telegram_baseurl,params=telegram_params)
    print(telegram_response)
    return
if __name__ == '__main__':
    video_alert()
