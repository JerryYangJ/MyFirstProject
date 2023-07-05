"""
    @ 函数：通过将一段有规律的、重复的代码定义为函数，来达到一次编写、多次调用的目的

    def functionname([parameterlist]):
        ['''conments''']
        [functionbody]

        functionname:   函数名称
        parameterlist：  可选参数，指定向函数中传递的参数。多个参数用逗号’，‘分隔。如果不指定，则表示没有参数，调用时也不指定参数
"""

import re


def re_demo():
    str1 = input('请输入需要查找的字符串：')
    str2 = input('请输入正则表达式：')
    print('需要查找的字符串为：'+'\n'+str(str1))
    print('输入的正则表达式为：'+'\n'+str(str2))
    result = re.findall(str2, str1)
    print(result)

re_demo()

def re_demo2():
    str1 = input('请输入需要查找的字符串：')
    str2 = input('请输入正则表达式：')
    print('需要查找的字符串为：'+'\n'+str(str1))
    print('输入的正则表达式为：'+'\n'+str(str2))
    result = re.findall(str2, str1)
    return result

result = re_demo2()
print(result)