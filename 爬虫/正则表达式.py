"""
    @ 正则表达式
        1.元字符
            ^   行的开始
            $   行的结尾
            .   匹配除换行符（\n)以外的任意字符
            \w  匹配字母、数字、下划线或汉字
            \s  匹配单个的空白符（包括Tab键和换行符）
            \S  除单个空白字符（包括Tab键和换行符）以外的所有字符
            \b  匹配单词的开始或结束，单词的分界符通常是空格，标点符号或者换行
            \d  匹配数字
        2.限定符
            ？       匹配前面的字符零次或一次
            +       匹配前面的字符一次或多次
            *       匹配前面的字符零次或多次
            {n}     匹配前面的字符n次
            {n,}    匹配前面的字符最少n次
            {n,m}   匹配前面的字符最少n次，最多m次
        3.排除字符
            [^]
        4.选择字符
            |   可以理解为”或“
        5.转义字符
            \   将特殊字符（如：“.”“？”“\”等）变为普通的字符

            '\\bm\\w*\\b'   模式字符串
            r'\bm\w*\b'     原生字符串（在模式字符串前加r或R，替代模式字符串中转移字符\的作用
    @re模块
        1.match()方法：从字符串开始处进行匹配，如果在起始位置匹配成功，则返回Match对象，否则返回None
            re.match(pattern,string,[flags])
                pattern:    模式字符串，由要匹配的正则表达式转换而来
                string:     要匹配的字符串
                flags:      可选参数，表示标志位，用于控制匹配方式，如是否区分大小写，常用标志如下：
                    A或ASCII     对于\w,\W,\b,\B,\d,\D,\s,\S只进行ASCII匹配
                    I或IGNORECASE    执行不区分字母大小写的匹配
                    M或MULTILINE     将^和$用于包括整个字符串的开始和结尾的每一行（默认仅适用于整个字符串的开始和结尾处）
                    S或DATALL        使用(.)字符匹配所有字符，包括换行符
                    X或VERBOSE       忽略模式字符串中未转义的空格和注释
        2.search()方法：在整个字符串中搜索第一个匹配的值，如果在起始位置匹配成品，则返回Match对象，否则返回None
            re.search(pattern,string,[flags])
        3.finaall()方法：在整个字符串中搜索所有符合正则表达式的字符串，并以列表的型式返回。如果匹配成功，则返回包含匹配结构的列表，否则返回空列表
            re.findall(pattern,string,[flags])
        4.sub()方法：用于实现字符串替换
            re.sub(pattern, repl, string, count, flags)
                pattern:    模式字符串，要由匹配的正则表达式转换而来
                repl:       替换的字符串
                string:     要被查找替换的原始字符串
                count：      可选参数，模式匹配后替换的最大次数，默认为0，表示替换所有的匹配
                flags:      可选参数，表示标志位，用于控制匹配方式，是否区分字母大小写
        5.分割字符
            re.split(pattern, string, [maxsplite], [flags])
                pattern:    模式字符串，要由匹配的正则表达式转换而来
                string:     要被查找替换的原始字符串
                maxsplite：  可选参数，最大的拆分次数
                flags:      可选参数，表示标志位，用于控制匹配方式，是否区分字母大小写

"""

import re


# match()方法
pattern = r'mr_\w+'     # 模式字符串
string1 = 'MR_SHOP mr_shop'     # 要匹配的字符串
string2 = '项目名称MR_SHOP mr_shop'
match1 = re.match(pattern, string1, re.I)    # 匹配字符串，不区分大小写
match2 = re.match(pattern, string2, re.I)    # 匹配字符串，不区分大小写
start = match1.start()      # 返回匹配值的其实位置
end = match1.end()          # 返回匹配值的结束位置
span = match1.span()         # 返回匹配位置的元组
string = match1.string       # 获取要匹配的字符串
print(match1, '\n', '开始位置为:', start, '\n', '结束位置为:', end, '\n', span, '\n', string,'\n', match2)

# search()方法
match3 = re.search(pattern, string1, re.I)
match4 = re.search(pattern, string2, re.I)
print(str(match3)+'\n'+str(match4))

# findall()方法
match5 = re.findall(pattern, string1, re.I)
match6 = re.findall(pattern, string2, re.I)
match7 = re.findall(pattern, string1)           # 区分大小写
match8 = re.findall(pattern, string2)
print(str(match5)+'\n'+str(match6)+'\n'+ str(match7)+'\n'+str(match8))

# 以下表达式不太理解？？？？？？？？？？？？？？？？？？？？？？？
pattern2 = r'[1-9]{1,3}(\.[0-9]{1,3}){3}'
string3 = '127.0.0.1 192.168.1.66'
match9 = re.findall(pattern2, string3)
print(match9)

# sub()方法
pattern3 = r'1[34578]\d{9}'
string4 = '中奖号码为：84978981 联系电话为：13611111111'
result =re.sub(pattern3, '1XXXXXXXXXX', string4)
match10 =re.findall(pattern3, string4)
print(match10)

# split()方法
pattern4 = r'[?|&]'
url = 'http://www.mingrisoft.com/login.jsp?usernama="mr"&pwd="mrsoft"'
result1 = re.split(pattern4, url)
print(result1)






