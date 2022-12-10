# @Time :2022/9/28 21:31
# @Author : Jerry Y
# @File  : B站太极拳视频.py
# @Info  :
import os
import re

import ffmpeg
import requests
from lxml import etree
import subprocess

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}

url = input('请输入B站视频播放地址：')
# url = f'https://www.bilibili.com/video/BV1xv4y1u7M1/?vd_source=927f6f12fc5e8e5f44d522566a9ead0e'
headers2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "referer": url
}
# 发送请求，获取源代码
resp = requests.get(url=url, headers=headers).text
tree = etree.HTML(resp)
# print(resp)

title = tree.xpath('//h1[@title]/text()')[0]
title = ''.join(title.split())
# ltitle = tree.xpath('//*[@id="bilibili-player"]//ul[contains(@class,"eplist")]/li[contains(@class,"state-active")]/text()')
# title = title.join(ltitle)
print(title)
# video_baseUrl_re = re.compile(r'"video":.*?baseUrl":"(.*?)",')
# audio_baseUrl_re = re.compile(r'"audio":.*?":"(.*?)",')
# video_baseUrl = video_baseUrl_re.findall(resp)
# audio_baseUrl = audio_baseUrl_re.findall(resp)
# # print(video_baseUrl[0])
# # print(audio_baseUrl[0])
# video = requests.get(url=video_baseUrl[0], headers=headers2)
# audio = requests.get(url=audio_baseUrl[0], headers=headers2)
# # print(video.status_code)
# # print(audio.status_code)
#
#
# with open(f'movie/{title}(视频).mp4', 'wb') as f:
#     f.write(video.content)
#
# with open(f'movie/{title}(音频).mp3', 'wb') as f:
#     f.write(audio.content)
#
# print(f'“{title}”下载完成')

# 合并音视频
# # 方法1(成功）：
# COMMAND = f'ffmpeg -i movie/{title}(视频).mp4 -i movie/{title}(音频).mp3 -c:v copy -c:a aac -strict experimental movie/{title}(音视频)(方法1).mp4'
# subprocess.run(COMMAND, shell=True)

# 方法2（成功）：
os.system('ffmpeg -i movie/{title}(视频).mp4 -i movie/{title}(音频).mp3 -c:v copy -c:a aac -strict experimental movie/{title}(音视频)(方法2).mp4')

# 方法3（成功）：
# input_video = ffmpeg.input(f'D:/pythonProject/爬虫/movie/{title}(视频).mp4')
# input_audio = ffmpeg.input(f'D:/pythonProject/爬虫/movie/{title}(音频).mp3')
# ffmpeg.concat(input_video, input_audio, v=1, a=1).output(f'D:/pythonProject/爬虫/movie/{title}(方法3).mp4').run()
# ffmpeg.concat(input_video, input_audio, v=1, a=1).output('movie/{title}(方法3).mp4').run(overwrite_output=True)