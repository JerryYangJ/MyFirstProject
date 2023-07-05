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
# os.system('ffmpeg -i D:/pythonProject/爬虫/movie/v.mp4 -i D:/pythonProject/爬虫/movie/a.mp3 -c:v copy -c:a aac -strict experimental D:/pythonProject/爬虫/movie/output(方法2).mp4')

# 方法3(成功）：
# input_video = ffmpeg.input(f'D:/pythonProject/爬虫/movie/v.mp4')
# input_audio = ffmpeg.input(f'D:/pythonProject/爬虫/movie/a.mp3')
# ffmpeg.concat(input_video, input_audio, v=1, a=1).output(f'D:/pythonProject/爬虫/movie/output(方法3).mp4').run()

# ffmpeg.concat(input_video, input_audio, v=1, a=1).output('movie/output(方法3).mp4').run(overwrite_output=True)



# 定义输入文件列表
input_files=[]
path = r'D:\pythonProject\爬虫\movie\25'
for i in range(1, 36):
    input_files.append(f'D:\pythonProject\爬虫\movie/25/{i}.ts')
print(input_files)

# 创建一个空的 ffmpeg 拼接过滤器
concat_filter = ffmpeg.concat(*[ffmpeg.input(file) for file in input_files], v=1, a=1)

# 输出文件
output_file = 'output.mp4'

# 执行合并操作
ffmpeg.output(concat_filter, output_file).run()