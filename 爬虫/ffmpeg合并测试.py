# @Time :2022/9/28 21:31
# @Author : Jerry Y
# @File  : ffmpeg合并音视频.py
# @Info  :
import subprocess

import ffmpeg
import os


# 合并音视频
# # 方法1(成功）：
# COMMAND = f'ffmpeg -i movie/v.mp4 -i movie/a.mp3 -c:v copy -c:a aac -strict experimental movie/output(方法1).mp4'
# subprocess.run(COMMAND, shell=True)

# 方法2（成功）：
# os.system('ffmpeg -i movie/v.mp4 -i movie/a.mp3 -c:v copy -c:a aac -strict experimental movie/output(方法2).mp4')

# 方法3(成功）：
input_video = ffmpeg.input(f'D:/pythonProject/爬虫/movie/v.mp4')
input_audio = ffmpeg.input(f'D:/pythonProject/爬虫/movie/a.mp3')
ffmpeg.concat(input_video, input_audio, v=1, a=1).output(f'D:/pythonProject/爬虫/movie/output(方法3).mp4').run()
# ffmpeg.concat(input_video, input_audio, v=1, a=1).output('movie/output(方法3).mp4').run(overwrite_output=True)