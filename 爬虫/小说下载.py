# @Time :2022/10/15 7:53
# @Author : Jerry Y
# @File  : 小说下载.py
# @Info  :
"""
拿到页面原代码 requests
通过re来提取想要的有效信息 re
"""
from urllib.parse import urljoin

import requests

from lxml import etree

base_url ='https://www.z1xs.com'
url ='https://www.z1xs.com/book/9651/'

# 请求头
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
headers = {
    "User-Agent": user_agent
}


# 发送ruquests请求，拿到页面源代码
resp = requests.get(url=url, headers=headers)
resp.encoding = 'GBK'
# print(resp.text)

tree = etree.HTML(resp.text)
name_list = tree.xpath('//*[@id="list"]/dl/dd/a/text()')
url_list = tree.xpath('//*[@id="list"]/dl/dd/a/@href')
# print(name_list, url_list)

for url in url_list:
    all_url = urljoin(base_url, url)
    # print(all_url)
    resp2 = requests.get(url=all_url, headers=headers)
    resp2.encoding='GBK'
    print(resp2.text)

    tree1 = etree.HTML(resp2.text)
    name = tree1.xpath('//h1/text()')
    content = tree1.xpath('//div[@id="content"]/text()')
    text = ''.join(content)
    print(text)
    with open(f'novel/{name[0]}.txt', 'ab') as f:
        f.write(text.encode('utf-8'))
