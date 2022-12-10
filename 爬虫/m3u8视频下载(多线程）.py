# @Time :2022/9/18 9:26
# @Author : Jerry Y
# @File  : m3u8视频下载.py
# @Info  :
from concurrent.futures import ThreadPoolExecutor

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}

base_url = [
    'https://qq1977134614.rx9696mv.com:8866/32aoe3yg-LZ4s69b8BIXWHDzt4xS3ueedmOkYh-hZc8YkhDNsJ56yBgpLnZPBRqf_NlvyRzZDBSd3yWZrB7S9A/',
    'https://qq1977134614.rx9696mv.com:8866/hGPaOmAXF6RYum25ROeTBbcXvUdhrhlyIWKrIJ07AeLmavb6n8rFcUlNAI9sfX02RhRWbVayFV24LMCZEBsyOA/',
    'https://qq1977134614.rx9696mv.com:8866/aC_fPf8GChN2wwAWbSdcgV9FnhCrdaQzHD8EuAn-1YMDcnTThTUl0YNA_INsBtr4n6yY69mZ_QzGDE-udw4Z2w/',
    'https://qq1977134614.rx9696mv.com:8866/oXuN4ihiW_0Y2FZfGruPMwDceNJ8LF2RyC6BvriKTxbp_yAoNgwSuFCjtQUGq1LkdOat7i_CUudnH2Kgow0brw/',
    'https://qq1977134614.rx9696mv.com:8866/1fF2bUMi27WG2ikkhNMPufsyEtGzemZ52aNCviZOEWtvoKQq3F2W3qAUPf8WLNLQPzDAvviKb5FdeoBQ7OdVsw/',
    'https://qq1977134614.rx9696mv.com:8866/ixeV1unconM-GTMsApd8OYxjn427OOcuqYVyqc7t4PPLY5Is3mE_o8mEfAGXAPy1QetAwosRFceRhNIreTp80A/',
    'https://qq1977134614.rx9696mv.com:8866/0G1hdIvo-uHVfwWa3cjFU42AqToObi8YKzCM6Q619MZbBDFbh-WC91eho3wHZrmwiNLSCB7PJKCJVLtQ5LxO0g/',
    'https://qq1977134614.rx9696mv.com:8866/W32HVJZFBLvVoWoLY9tQzcQFdWtvGDHHtUvZbsF413mlH8UD-QQSK67217vuqX2NF0zJXwyMKkCyYYjLehpr1Q/',
    'https://qq1977134614.rx9696mv.com:8866/dzXvYOUdr8Hu7VFWZ_Z6IvnQ-nSHU89yPwh9ElRHQU4c8rFr7ydPM6w3KVU7yoluA5XZIfhv_fEG93aPtBWjag/',
    'https://qq1977134614.rx9696mv.com:8866/-oIvQ03xTxzEznJi5T8syVLsnfv96mOb_l2lzfm-qmtBasdJOUuYoCjK1pBsPkA1V_xT6WcXKLdr5iNaK4lgdw/',
    'https://qq1977134614.rx9696mv.com:8866/bROOyYcJk8aXWf_wJ37Oi_raZEwyMRWZgWx07EfTdsYZjT_1eFtsGkgsdsZR9w8rXCpJ2Jp5P6mh_k2FHJ4FBQ/',
    'https://qq1977134614.rx9696mv.com:8866/ewM52t3CeAA77C4l-0bRZ5ml50Ud1lpHi_olOM-j3XcZ3uuKj-ffWgMZ1m91JFpl23JsUnMtrf0XYXn9tqvldQ/'
]


# 1.向m3u8网址发送请求，获取m3u8文件

# 2.读取m3u8文件，提取下载链接。
def down_m3u8(m3u8_num):
    n = 1
    with open(f'./movie/m3u8/{m3u8_num}.m3u8', 'r') as f:
        print(m3u8_num)
        for line in f:
            line = line.strip()
            if not line.startswith("#"):
                with ThreadPoolExecutor(50) as t:
                    t.submit(down_ts, m3u8_num, line, n)
                    n += 1


def down_ts(i, line, n):
    down_url = base_url[i - 1] + line
    # print(down_url)
    # 3.向视频片段下载链接发送请求，获取数据。
    resp = requests.get(url=down_url, headers=headers)
    # 4.存储数据
    f = open(f'./movie/m3u8_1/{i}/{n}.ts', mode='wb')
    f.write(resp.content)
    print(f'{i}-{n}完成下载')
    n += 1


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 13):
            print(i)
            t.submit(down_m3u8, i)
# 5.合并数据
