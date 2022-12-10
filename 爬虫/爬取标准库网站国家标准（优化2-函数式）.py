"""
拿到页面原代码 requests
通过re来提取想要的有效信息 re
"""

import requests
import re
import time

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'

index_url = "http://www.bzko.com/std/GJBZ/List_1327.html"
child_url1 = "http://www.bzko.com/std/"
download_url_1 = "http://www.bzko.com/Common/ShowDownloadUrl.aspx?urlid=0&id="
headers = {
    "User-Agent": user_agent
}
headers1 = {
    "User-Agent": user_agent,
    "Referer": "http://www.bzko.com/std/GJBZ/"
}


# 发送ruquests请求，拿到页面源代码
def set_requests(url, headers):
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    pages = resp.text
    resp.close()
    return pages


# 发送session请求，拿到页面源代码
def set_session(url, headers):
    session = requests.session()
    resp = session.get(url, headers=headers)
    resp.encoding = 'utf-8'
    pages = resp.text
    return pages, session


# 解析主页面，拿到子页面url地址、文件名称和ID
def parse_index_pages(pages):
    # 使用正则表达式解析数据
    obj = re.compile(
        r'<div class="childclasslist_title.*?<div class="childclasslist_time">.*?<a href=".*?/std/(?P<url_id>.*?).html" target="_blank">(?P<name>.*?)</a>',
        re.S)
    # 开始匹配
    result = obj.finditer(pages)
    # 创建一个url空列表,存储第二层页面地址;创建一个空列表存储download_id
    child_url_list = []
    url_id_list = []
    name_list = []
    for it in result:
        # 拼接子页面地址
        url_id = it.group("url_id")
        name = it.group("name").strip().replace("/", ' ')
        child_url = child_url1 + url_id + '.html'
        # 将拼接的子页面地址加入到子页面list中
        child_url_list.append(child_url)
        url_id_list.append(url_id)
        name_list.append(name)
    return child_url_list, name_list, url_id_list


def parse_child_pages(pages):
    # 解析源代码，提取下载链接url
    obj1 = re.compile(r'<div id="content">.*?href="(?P<download_url_rel>.*?)".*?点击下载该标准</a>', re.S)
    download_url = obj1.findall(pages)
    return download_url


# 写入文件
def write_to_file(name, data):
    with open(name, 'wb') as f:
        f.write(data)
    print(name, "下载完成")


keyword = '管'

for n in range(1320, 1327):  # 一共1327页，先
    index_url = f"http://www.bzko.com/std/GJBZ/List_{n}.html"
    index_resp = requests.get(index_url, headers)
    index_resp.encoding = 'utf-8'
    pages = index_resp.text
    index_resp.close()

    url_name_id_list = parse_index_pages(pages)

    for i in range(50):
        if keyword in url_name_id_list[1][i]:
            # print('子页面的地址前缀为：', url_name_id_list[0])
            # print(f'第{i}个子页面地址为：', url_name_id_list[0][i])  # http://www.bzko.com/std/243625.html
            print(f'第{i}个文件名称为：', url_name_id_list[1][i])
            # print(f"第{i}个文件ID为：", url_name_id_list[2][i])

            session = requests.session()

            # child_pages = session.get(child_url, headers=headers1)
            # child_pages.close()
            show_download_url = download_url_1 + url_name_id_list[2][i]
            print('显示下载页面地址：', show_download_url)

            headers2 = {
                "User-Agent": user_agent,
                "Referer": url_name_id_list[0][i]
            }
            show_download_pages = session.get(show_download_url, headers=headers1)
            show_download_pages.close()
            show_download_pages.encoding = 'utf-8'
            show_download_pages = show_download_pages.text
            reall_url = parse_child_pages(show_download_pages)

            print('真正的下载地址：', reall_url[0])
            headers3 = {
                "User-Agent": user_agent,
                "Referer": show_download_url
            }
            data = session.get(reall_url[0], headers=headers3).content
            write_to_file(f'./GB国标/{url_name_id_list[1][i]}.rar', data)
            time.sleep(10)
        else:
            time.sleep(10)
            continue
