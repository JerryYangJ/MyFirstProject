str1 = "我是日丰人wsrfr"
con = len(str1)

i=0
while i < con:
    str2 = str1[i]
    i = i + 1
    print(str2)

bool1 = str1.endswith("我")    # 检查字符串的结束字符是否以参数结束。如果是，返回True，否则false
print(bool1)

bool2 = str1.title()
print(bool2)