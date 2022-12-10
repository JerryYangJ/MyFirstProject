"""
拿到页面原代码 requests
通过re来提取想要的有效信息 re
"""

import requests
import re


# 拿到源代码
url = "https://movie.douban.com/top250"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}
resp = requests.get(url, headers=headers)
page_content = resp.text

# 使用正则表达式解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)人评价</span>',re.S)
# 开始匹配
result = obj.finditer(page_content)
for it in result:
    print(it.group("name"))
    print(it.group("year").strip())
    print(it.group("score"))
    print(it.group("num"))





