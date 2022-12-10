# @Time :2022/9/18 9:26
# @Author : Jerry Y
# @File  : m3u8视频下载.py
# @Info  :
import re
import time

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}


m3u8_base = 'https://kankanb.35ju.com:1234/jxplayer.php?'
ts_base_list = []

if __name__ == '__main__':
    n = 1
    # 1.向每集的页面发送请求，获取v的值.获取m3u8文件的获取地址
    for i in range(0, 12):
        index_url = f'https://www.39xp.com/kb/78659-0-{i}.html'
        resp = requests.get(url=index_url, headers=headers)
        v_re = re.compile(f'var now="(.*?)"')
        v = v_re.findall(resp.text)[0]
        resp.close()
        print(v)
        # m3u8页面地址
        m3u8_url = m3u8_base + v
        print(m3u8_url)

        # 向m3u8文件获取地址页面发送请求，解析m3u8地址
        resp1 = requests.get(url=m3u8_url, headers=headers)
        m3u8_re = re.compile(f'var urls = "(.*?)"')
        m3u8_rel_url = m3u8_re.findall(resp1.text)[0]
        resp1.close()
        print(m3u8_rel_url)
        ts_base = m3u8_rel_url.replace(f'RongXingVR.m3u8', '')
        print(ts_base)
        ts_base_list.append(ts_base)

        # 2.向m3u8页面地址发送请求，下载m3u8文件
        resp2 = requests.get(url=m3u8_rel_url, headers=headers)
        with open(f'./movie/m3u8/{i + 1}.m3u8', 'wb') as f:
            f.write(resp2.content)
        resp2.close()

        # 4.读取真正的m3u8文件，获取ts下载地址
        with open(f'./movie/m3u8/{i+1}.m3u8', 'r') as f1:
            for ts_line in f1:
                ts_line = ts_line.strip()
                if not ts_line.startswith("#"):
                    # print(f'读取第{i}集ts地址{ts_line}，准备下载')
                    # 3.向视频片段下载链接发送请求，获取数据。
                    ts_line = ts_base_list[i] + ts_line
                    resp = requests.get(url=ts_line, headers=headers)
                    # 4.存储数据
                    with open(f'./movie/m3u8_1/{i + 1}/{n}.ts', mode='wb') as f2:
                        f2.write(resp.content)
                        print(f'{i+1}-{n}完成下载')
                    resp.close()
                    n += 1
                    time.sleep(0.5)

