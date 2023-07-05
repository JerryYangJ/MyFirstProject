"""
@author: JerryYang
@file: 数据解析方法3-BS4（练习）.py
@time: 2023/6/30 14:06
@desc:
"""
from bs4 import BeautifulSoup

# fp就表示本地存储的一个html文件
fp = open('BS4_test.html', 'r', encoding='utf-8')
# 解析本地存储的html文件中的内容
# 实例化BeautifulSoup对象，然后把即将被解析的页面源码数据加载到了该对象中
soup = BeautifulSoup(fp, 'lxml')  # 参数2，lxml是固定形式，表示指定的解析器

# 标签定位

# 方式1：soup.tagName,只会定位到符合条件的第一个标签
# tag1 = soup.title  # 定位到了title标签
# print(tag1.text)
# tag2 = soup.div
# print(tag2.text)

# 方式2：属性定位，find函数，findall函数
# find('tagName',attrName='attrValue')：find只会定位到满足要的第一个标签
tag3 = soup.find('div', class_='song')  # 定位class属性值为song的div标签
print(tag3.text)
tag4 = soup.find('a', id='feng')  # 定位id属性值为feng的a标签
print(tag4.text)
# findAll('tagName',attrName='attrValue')：可以定位到满足要求的所有标签
tag5 = soup.findAll('div', class_='song')
for i in tag5:
    print(i.text)
#
# # 方式3：选择器定位：soup.select('选择器')
# # id选择器：#feng  ----id为feng
# # class选择器：.song ----class为song
# # 层级选择器：大于号表示一个层级，空格表示多个层级
# tag6 = soup.select('#feng')  # 定位到所有id属性值为feng的标签
# tag7 = soup.select('.song')  # 定位到所有class属性值为song的标签
# tag8 = soup.select('.tang > ul > li')  # 定位到了class为tang下面的ul下面所有的li标签
# tag9 = soup.select('.tang li')
#
# # 提取标签中的内容
# # 1.提取标签中间的内容：
# # tag.string:只可以提取到标签中直系的文本内容
# # tag.text:可以提取到标签中所有的文本内容
# p_tag = soup.p
# print(p_tag.string)
# print(p_tag.text)
# div_tag = soup.find('div',class_='song')
# print(div_tag.text)
#
# # 2.提取标签的属性值
# # tag['attrName']
# img_tag = soup.img
# print(img_tag['src'])  # 提取img标签的src的属性值
