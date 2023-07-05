# @Time :2022/9/18 9:26
# @Author : Jerry Y
# @File  : m3u8视频下载.py
# @Info  :

# https://www.gzjslzs.com/k/96209-0-0.html
import requests

from Crypto.Cipher import AES
from concurrent.futures import ThreadPoolExecutor



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"

}


def down_ts(ts_line, n):
    # 向视频片段下载链接发送请求，获取数据。
    ts_resp = requests.get(url=ts_line, headers=headers)
    data = ts_resp.content
    key = '30692406d8df9bff'
    iv = b'0000000000000000'
    cryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    # 4.存储数据
    with open(f'D:\下载/1/{n}.ts', mode='wb') as f2:
        f2.write(cryptor.decrypt(data))
    ts_resp.close()
    print(f'{n}完成下载')


if __name__ == '__main__':
    ts_line_list = []
    with ThreadPoolExecutor(20) as t:
        with open(f'D:\下载\index (1).m3u8', 'r') as f1:
            for ts_line in f1:
                ts_line = ts_line.strip()
                if not ts_line.startswith("#"):
                    ts_line_list.append(ts_line)
            for i, ts_line in enumerate(ts_line_list):
                t.submit(down_ts, ts_line, i)
                print(i, ts_line)


