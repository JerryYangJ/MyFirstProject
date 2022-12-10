"""
拿到页面原代码 requests
通过re来提取想要的有效信息 re
"""

import requests
import re

# 拿到主页源代码
url = "http://www.bzko.com/std/GJBZ/"
url1 = "http://www.bzko.com/std/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
page_content = resp.text

# 使用正则表达式解析数据
# obj = re.compile(r'<div>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
#                  r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
#                  r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
#                  r'.*?<span>(?P<num>.*?)人评价</span>',re.S)
obj = re.compile(
    r'<div class="childclasslist_title.*?<div class="childclasslist_time">.*?<a href=".*?/std/(?P<url_id>.*?).html" target="_blank">(?P<name>.*?)</a>',
    re.S)
# 开始匹配
result = obj.finditer(page_content)

# 创建一个url空列表,存储第二层页面地址;创建一个空列表存储download_id
child_url_list = []
url_id_list = []
for it in result:
    # 拼接子页面地址
    url_id = it.group("url_id")
    child_url = url1 + url_id + '.html'
    # 将拼接的子页面地址加入到子页面list中
    child_url_list.append(child_url)
    url_id_list.append(url_id)
print("最后一个：", child_url_list[-1])
print("最后一个ID：", url_id_list[-1])

# 向第二层showdownurl子页面发送请求，拿到子页面代码，这里需要从主页面跳转，否则服务器拒绝。
url2 = child_url_list[-1]  # "http://www.bzko.com/std/243046.html"

headers2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "Referer": "http://www.bzko.com/std/GJBZ/"
}

resp2 = requests.get(url2, headers=headers2)
resp2.encoding = "utf-8"
child_page_content = resp2.text
# print(child_page_content)

# 第三层：下载页(此页请求有防盗链，但无需Cookie，需要在此页使用会话用于下载请求)
download_url_1 = "http://www.bzko.com/Common/ShowDownloadUrl.aspx?urlid=0&id="
download_id_1 = "243046"
download_url = download_url_1 + download_id_1

headers3 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "Referer": url2
}
# resp3 = requests.get(download_url, headers=headers3)
session = requests.session()
resp3 = session.get(download_url, headers=headers3)
resp3.encoding = "utf-8"
download_page_content = resp3.text
# print(download_page_content)

# 解析源代码，提取下载链接url
obj1 = re.compile(r'<div id="content">.*?href="(?P<download_url_rel>.*?)".*?点击下载该标准</a>', re.S)

result1 = obj1.findall(download_page_content)

print('实际下载地址：', result1)

# 下载需要Cookie,如何处理？？？？？？？？？？？？？？？？？——————>下载页需要创建会话（记录Cookie)，通过会话请求下载
headers4 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46",
    # "Cookie": "UM_distinctid=17fb550140fa3b-0b1e0a5b120538-5617185b-1fa400-17fb5501410b07; __gads=ID=f9a3f24e27eeddbe-22f47b2819d100e3:T=1648014401:RT=1648014401:S=ALNI_MaIhDxw-q1mzkTGUm5_2Xg-KoYfXw; safedog-flow-item=99E2FB4D0BC04643B025421158C9C59A; IISSafeDogLGSession=BF4928DBAAF0F23626A9204E9CA637E8",
    "Referer": download_url
}


# 向下载链接发送请求，接收、保存目标数据
with open('31.rar', mode='wb') as f:
    f.write(session.get(result1[0], headers=headers4).content)

