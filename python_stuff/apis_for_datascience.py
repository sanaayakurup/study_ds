# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:59:27 2022

@author: sanaayak
"""
#https://www.youtube.com/watch?v=fklHBWow8vE&t=274s

import requests #allows us to make api calls
import time
import pandas as pd


API_KEY='AIzaSyA5OkPHS5W-kFqdg8s92L3voZv3G0mr1qE'
CHANNEL_ID='UCW8Ews7tdKKkBT6GdtQaXvQ'
pageToken=""
url = "https://www.googleapis.com/youtube/v3/search?key="+API_KEY+"&channelId="+CHANNEL_ID+"&part=snippet,id&order=date&maxResults=10000&"+pageToken
#make an api call
response=requests.get(url).json()


df=pd.DataFrame(columns=['video_id','video_title','upload_date'])
#now we extract the important stuff 
for video in response['items']:
        if video['id']['kind']=='youtube#video':
            video_id=video['id']['videoId']
            video_title=video['snippet']['title']
            video_title=str(video_title).replace("@amp;","")
            upload_date=video['snippet']['publishedAt']
            upload_date=upload_date.split(sep='T')[0]
            
            #save data in pd df
            df=df.append({'video_id':video_id,'video_title':video_title,'upload_date':upload_date},ignore_index=True)
            