# @Time :2022/9/18 9:26
# @Author : Jerry Y
# @File  : m3u8视频下载.py
# @Info  :
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}

base_url1 = 'https://qq1977134614.rx9696mv.com:8866/32aoe3yg-LZ4s69b8BIXWHDzt4xS3ueedmOkYh-hZc8YkhDNsJ56yBgpLnZPBRqf_NlvyRzZDBSd3yWZrB7S9A/'
base_url2 = 'https://qq1977134614.rx9696mv.com:8866/hGPaOmAXF6RYum25ROeTBbcXvUdhrhlyIWKrIJ07AeLmavb6n8rFcUlNAI9sfX02RhRWbVayFV24LMCZEBsyOA/'
base_url3 = 'https://qq1977134614.rx9696mv.com:8866/aC_fPf8GChN2wwAWbSdcgV9FnhCrdaQzHD8EuAn-1YMDcnTThTUl0YNA_INsBtr4n6yY69mZ_QzGDE-udw4Z2w/'
base_url4 = 'https://qq1977134614.rx9696mv.com:8866/oXuN4ihiW_0Y2FZfGruPMwDceNJ8LF2RyC6BvriKTxbp_yAoNgwSuFCjtQUGq1LkdOat7i_CUudnH2Kgow0brw/'
base_url5 = 'https://qq1977134614.rx9696mv.com:8866/1fF2bUMi27WG2ikkhNMPufsyEtGzemZ52aNCviZOEWtvoKQq3F2W3qAUPf8WLNLQPzDAvviKb5FdeoBQ7OdVsw/'
base_url6 = 'https://qq1977134614.rx9696mv.com:8866/ixeV1unconM-GTMsApd8OYxjn427OOcuqYVyqc7t4PPLY5Is3mE_o8mEfAGXAPy1QetAwosRFceRhNIreTp80A/'
base_url7 = 'https://qq1977134614.rx9696mv.com:8866/0G1hdIvo-uHVfwWa3cjFU42AqToObi8YKzCM6Q619MZbBDFbh-WC91eho3wHZrmwiNLSCB7PJKCJVLtQ5LxO0g/'
base_url8 = 'https://qq1977134614.rx9696mv.com:8866/W32HVJZFBLvVoWoLY9tQzcQFdWtvGDHHtUvZbsF413mlH8UD-QQSK67217vuqX2NF0zJXwyMKkCyYYjLehpr1Q/'
base_url9 = 'https://qq1977134614.rx9696mv.com:8866/dzXvYOUdr8Hu7VFWZ_Z6IvnQ-nSHU89yPwh9ElRHQU4c8rFr7ydPM6w3KVU7yoluA5XZIfhv_fEG93aPtBWjag/'
base_url10 = 'https://qq1977134614.rx9696mv.com:8866/-oIvQ03xTxzEznJi5T8syVLsnfv96mOb_l2lzfm-qmtBasdJOUuYoCjK1pBsPkA1V_xT6WcXKLdr5iNaK4lgdw/'
base_url11 = 'https://qq1977134614.rx9696mv.com:8866/bROOyYcJk8aXWf_wJ37Oi_raZEwyMRWZgWx07EfTdsbl7RtO_6QnJM21H7_qqV-C0r9824jITPd6CtjNBfrAYg/'
base_url12 = 'https://qq1977134614.rx9696mv.com:8866/ewM52t3CeAA77C4l-0bRZ5ml50Ud1lpHi_olOM-j3XcZ3uuKj-ffWgMZ1m91JFpl23JsUnMtrf0XYXn9tqvldQ/'
# 1.向m3u8网址发送请求，获取m3u8文件

# 2.读取m3u8文件，提取下载链接。
n = 1
i = 5
with open(f'./movie/m3u8/{i}.m3u8', 'r') as f:
    for line in f:
        line = line.strip()
        if not line.startswith("#"):
            down_url = base_url8 + line
            print(down_url)
            # 3.向视频片段下载链接发送请求，获取数据。
            resp = requests.get(url=down_url, headers=headers)
            # 4.存储数据
            f = open(f'./movie/m3u8_1/{i}/{n}.ts', mode='wb')
            f.write(resp.content)
            n += 1

# 5.合并数据
