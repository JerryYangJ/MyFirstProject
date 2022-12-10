"""
    @ 常用字符串类型：str   bytes
        str：    Unicode字符（ASCII或者其他）
        bytes：  二进制数据（包括编码的文本）

    @ 通过encode()和decode()方法可以进行str、bytes类型之间的转换
        1.使用encode()方法编码：将字符串转换为二进制数据（即btyes），即”编码“
            str.encode([encoding = "utf-8"][,errors = "strict"]}
                str:    要进行转换的字符串
                encoding="utf-8":   可选参数，指定转码时采用的字符编码，默认为UTF-8. 简体中文为gb2312
                errors=”strict“：    可选参数，指定错误处理方式。strict抛出异常、ignore忽略、replace用？替换、xmlcharrefreplace用XML的字符引用
        2.使用decode()方法解码：将使用encode()方法转换的结果再转换为字符串，即”解码“
            bytes.decode([encoding = "utf-8"][,errors = "strict"]}
                bytes:要进行转换的二进制数据，通常是encode()方法转换的结果
                encoding="utf-8":   可选参数，指定转码时采用的字符编码，默认为UTF-8. 简体中文为gb2312
                errors=”strict“：    可选参数，指定错误处理方式。
"""

verse = '天道酬勤'
bytes = verse.encode('GBK')
verse1 = bytes.decode("GBK")
print('原字符串：', verse)
print('编码后：', bytes)
print('解码后：', verse1)
