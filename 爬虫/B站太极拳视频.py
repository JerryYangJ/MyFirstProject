# @Time :2022/9/28 21:31
# @Author : Jerry Y
# @File  : B站太极拳视频.py
# @Info  :

import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}

for page in [8,]:
    url = f'https://www.bilibili.com/video/BV1iE411c7Ni/?p={page}&vd_source=927f6f12fc5e8e5f44d522566a9ead0e'
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
        "referer": url
    }
    # 发送请求，获取源代码
    resp = requests.get(url=url, headers=headers).text
    # print(resp)

    video_baseUrl_re = re.compile(r'"video":.*?baseUrl":"(.*?)",')
    video_baseUrl = video_baseUrl_re.findall(resp)
    print(video_baseUrl[0])
    video = requests.get(url=video_baseUrl[0], headers=headers2)
    print(video.status_code)

    audio_baseUrl_re = re.compile(r'"audio":.*?":"(.*?)",')
    audio_baseUrl = audio_baseUrl_re.findall(resp)
    print(audio_baseUrl[0])

    audio = requests.get(url=audio_baseUrl[0], headers=headers2)
    print(audio.status_code)

    with open(f'./movie/太极/{page}.mp4', 'wb') as f:
        f.write(video.content)

    with open(f'./movie/太极1/{page}.mp4', 'wb') as f:
        f.write(audio.content)

