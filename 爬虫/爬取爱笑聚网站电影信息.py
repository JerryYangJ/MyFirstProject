"""
拿到页面原代码 requests
通过re来提取想要的有效信息 re


"""

import requests
import re
import time

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'

# n = 1
# 拿到主页源代码
index_url = "https://www.axjbt.com/"  # 主页地址


headers = {
    "referer": index_url,
    "User-Agent": user_agent
}


# 发送ruquests请求，拿到页面源代码
def set_requests(url, headers):
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    pages = resp.text
    resp.close()
    return pages


'''

'''


# 解析主页面，拿到url链接地址
def index_parse_pages(pages):
    # 使用正则表达式解析数据
    # print(pages)
    obj = re.compile(
        r'<a href="/read-(?P<id>.*?)".*?get="_blank">.*?<img.*?</span>(?P<name>.*?)</p></a>', re.S)
    # 开始匹配
    result = obj.findall(pages)
    print(result)
    return result


# r'<div id="info">.*?导演</span>: <(?P<film_director>.*?)></p>.*?类型:</span>(?P<film_class>.*?)</p>.*?上映日期:</span>(?P<date>.*?)</p>',
# 解析详情页，拿到电影导演、类型、上映日期、公开的下载链接
def detail_parse_pages(pages):
    # print(pages)
    # info_list=[]
    # # 使用正则表达式解析数据
    # obj = re.compile(
    #     r'<h2>(?P<film_name>.*?)</h2>.*?<div id="info">.*?导演</span>:(?P<film_director>.*?)</p>.*?类型:</span>(?P<film_class>.*?)</p>.*?>上映日期:</span>(?P<date>.*?)</p>',
    #     re.S
    # )
    # # 开始匹配
    # result = obj.finditer(pages)
    # for it in result:
    #     film_name = it.group("film_name").strip()
    #     film_director = it.group("film_director").strip()
    #     film_class = it.group("film_class").strip()
    #     date = it.group("date").strip()
    #     info_list = [film_name, film_director, film_class, date]
    #     # print(film_name, film_director, film_class, date)
    # obj1 = re.compile(
    #     r'<li>.*?公开.*?<a rel="nofollow" href=(.*?)>',
    #     re.S
    # )
    # result1 = obj1.findall(pages)
    # # print(result1)
    # info_list.append(result1)
    # return info_list
    obj1 = re.compile(
        r'<li>.*?公开.*?<a rel="nofollow" href=(.*?)>', re.S)
    result1 = obj1.findall(pages)
    return result1 


# 写入文件
def write_to_file(name, data):
    with open(name, 'a', encoding='utf-8') as f:
        f.write(data)
    # print(name, "完成")

for n in range(1, 4):
    child_url = f"https://www.axjbt.com/thread-5-{n}"  # 欧美篇地址
    pages = set_requests(child_url, headers)

    id_name_list = index_parse_pages(pages)

    for i in id_name_list:
        print(i)

    for i in range(0, len(id_name_list)):
        # detail页地址
        detail_url = index_url + 'read-' + id_name_list[i][0]
        f_name = id_name_list[i][1]
        print(f_name, detail_url)

        detail_pages = set_requests(detail_url, headers)
        info = detail_parse_pages(detail_pages)
        print(info)
        for data in info:
            data = ''.join(data.strip())
            write_to_file('111.txt', f_name)
            write_to_file('111.txt', '\n')
            write_to_file('111.txt', data)
            write_to_file('111.txt', '\n')

print(f"第{n}页完成")



