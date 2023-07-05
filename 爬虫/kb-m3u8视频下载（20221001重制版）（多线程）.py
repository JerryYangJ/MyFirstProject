# @Time :2022/9/18 9:26
# @Author : Jerry Y
# @File  : m3u8视频下载.py
# @Info  : 网址：https://www.bei-fa.com/vodplay/36867-1-4.html（最后一位数字是集数）
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"

}

episode = ''
url = f'https://www.bei-fa.com/vodplay/36867-1-{episode}.html'


def get_m3u8():
    """ 获取每集的m3u8文件 """
    # 向每集地址发送请求，获取源代码，提取m3u8请求地址
    for episode in range(1, 2):
        m3u8_index_rep = requests.get(url=url, headers=headers)
        print(m3u8_index_rep.text)
        m3u8_re = re.compile(f'"url":"(.*?)"')
        m3u8_index = m3u8_re.findall(m3u8_index_rep.text)
        print(m3u8_index)


def down_ts(ts_line, episode, ts_name):
    # 写文件前判断文件存储路径是否存在，不存在则创建路径
    save_path = f'./movie/{episode}/'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
        time.sleep(1)
    # 向视频片段下载链接发送请求，获取数据。
    try:
        ts_resp = requests.get(url=ts_line, headers=headers)
        with open(f'{save_path}/{ts_name}.ts', mode='wb') as f2:
            f2.write(ts_resp.content)
        ts_resp.close()
        print(f'{ts_name}完成下载', ts_line)
    except:
        print(ts_line, ts_name, "未成功下载")
        try:
            print(f"正在重试第{ts_name}：", ts_line, ts_name)
            ts_resp = requests.get(url=ts_line, headers=headers)
            with open(f'{save_path}/{ts_name}.ts', mode='wb') as f2:
                f2.write(ts_resp.content)
            ts_resp.close()
            print(f'{ts_name}完成下载', ts_line)
        except:
            print(f"重试第{ts_name}失败，请手工下载：", ts_line)


if __name__ == '__main__':
    with ThreadPoolExecutor(8) as t:
        # 读取m3u8文件，下载ts
        for episode in range(25, 26):
            n = 1
            with open(f'./movie/m3u8/{episode}.m3u8', 'r') as f:
                for ts_line in f:
                    ts_line = ts_line.strip()
                    if not ts_line.startswith("#"):
                        # print(ts_line)
                        t.submit(down_ts, ts_line, episode, n)
                        print(ts_line, n, "已提交")
                        n += 1
                print(f"第{episode}集下载提交完成")
    print("所有集数下载完成")

    # 下载完成后，用ffmpeg合并ts文件
    # os.system(f'ffmpeg -f concat -safe 0 -i D:/pythonProject/爬虫/movie/ts.txt -c copy D:\pythonProject\爬虫\movie\TS Merger tools\Merger\5.mp4')

"""
不保存m3u8，直接下载：
url = "https://new.qqaku.com/20221023/1DhUmOUv/1100kb/hls/index.m3u8"
resp = requests.get(url=url, headers=headers).text
index_list = re.findall(r'https(.*?).ts', resp)
ts_urls = []
for i in index_list:
    title = i.split("/")[-1]
    ts_url = "https" + i + ".ts"
    ts_urls.append(ts_url)
start_time = time.time()

# 实例化一个线程池对象
pool = Pool(30)
# 将列表中的每一个列表元素传递给get_content中进行处理。
content = pool.map(get_content, ts_urls)

end_time = time.time()
print('%d second'% (end_time-start_time))
pool.close()
pool.join()
"""
