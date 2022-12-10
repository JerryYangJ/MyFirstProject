import re


while True:
    str1 = input('请输入需要查找的字符串：')
    str2 = input('请输入正则表达式：')
    print('需要查找的字符串为：'+'\n'+str(str1))
    print('输入的正则表达式为：'+'\n'+str(str2))
    result = re.findall(str2, str1)
    print(result)

