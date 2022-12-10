import re

html="""
<div><p>www.biancheng.net</p></div>
<div><p>编程帮</p></div>
"""

data = re.compile(r'<div><p>(.*?)</p')
result = data.findall(html)
print(result)
"""
#贪婪匹配，re.S可以匹配换行符
#创建正则表达式对象
pattern=re.compile('<div><p>.*</p></div>',re.S)
#匹配HTMLX元素，提取信息
re_list=pattern.findall(html)
print(re_list)
#非贪婪模式匹配，re.S可以匹配换行符
pattern=re.compile('<div><p>.*?</p></div>',re.S)
re_list=pattern.findall(html)
print(re_list)
"""
