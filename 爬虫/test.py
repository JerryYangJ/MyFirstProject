from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
# for link in soup.find_all('a'):
#     print(link.get('href'))
# print(soup.get_text())
# print(soup.getText)

# 一、查找tag对象
print(soup.head, type(soup.head))
print(soup.title, type(soup.title))
print(soup.a, type(soup.a))  # 第一个a标签，如果想获取所有a标签要用到soup.find_all('a')
print(soup.p.b)

# 二、查找tag对象的标签名和属性
print(soup.a.name)  # a
print(soup.p.b.name)  # b
print(soup.a["href"])
print(soup.a.attrs)

'''
三、
HTML 4定义了一系列可以包含多个值的属性.在HTML5中移除了一些,却增加更多.
最常见的多值的属性是 class (一个tag可以有多个CSS的class). 
还有一些属性 rel , rev , accept-charset , headers , accesskey . 
在Beautiful Soup中多值属性的返回类型是list
'''

print(soup.a["class"])  # 返回列表

# 四、tag的属性可以被添加,删除或修改(tag的属性操作方法与字典一样)
# soup.a["class"] = ["sister c1"]
# del soup.a["id"]
# print(soup)

# 五、获取标签对象的文本内容
print(soup.p.string)  # p下的文本只有一个时，取到，否则为None
print(soup.p.strings)  # 拿到一个生成器对象, 取到p下所有的文本内容
for i in soup.p.strings:
    print(i)
# 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None，如果只有一个子节点那么就输出该子节点的文本，比如下面的这种结构，soup.p.string 返回为None,但soup.p.strings就可以找到所有文本
p2 = soup.find_all("p")[1]
print(p2.string)
print(p2.strings)
for i in p2.strings:
    print(i)
# text 和 string
print(soup.p.string)
print(soup.p.text)  # 取到p下所有的文本内容,text属性更常用，并且它可以直接过滤掉注释
print(p2.text)

# 遍历文档树（导航文档树）

# 1、嵌套选择
print(soup.head.title.text)
print(soup.body.a.text)

# 2、子节点、子孙节点
print(soup.p.contents)  # p下所有子节点
print(soup.p.children)  # 得到一个迭代器,包含p下所有子节点

for i, child in enumerate(soup.p.children, 1):
    print(i, child)

print(soup.p.descendants)  # 获取子孙节点,p下所有的标签都会选择出来
for i, child in enumerate(soup.p.descendants, 1):
    print(i, child)
for i, child in enumerate(soup.find_all("p")[1].descendants, 1):
    print(i, child)

# 3、父节点、祖先节点
print(soup.a.parent)  # 获取a标签的父节点
print(soup.a.parent.text)  # 获取a标签的父节点
print(soup.a.parents)  # 找到a标签所有的祖先节点，父亲的父亲，父亲的父亲的父亲...

# 4、兄弟节点
print("===")
print(soup.a.next_sibling)  # 下一个兄弟,类型：<class 'bs4.element.NavigableString'>
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling.previous_sibling)
print(soup.a.previous_siblings)  # 上面的兄弟们=>生成器对象

# 搜索文档树
