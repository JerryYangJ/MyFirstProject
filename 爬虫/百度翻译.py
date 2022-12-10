# @Time :2022/11/29 11:31
# @Author : Jerry Y
# @File  : 百度翻译.py
# @Info  :

import execjs
import requests

while True:
    word = input("请输入您要翻译的词语：")
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Acs-Token': '1669619087310_1669692580457_7gFLkTLeutQbHqhHgJwtwI51EMQDLsHYtnsf3n2YpJi9YqlksPqF6Afmvzkdq8/ojj/CfRl1h+dlKa4jpD47mLkT1fQx6WQ0Gii1ntYxReY2TnktM/r8qrNV5NQ+OyUclh+M6JlO071hdWrCIpvROddYZ2Pm+ku6M7mDu5PrvoQKPZsXygQ72MF9/sbrQM8NzTuhBaf6R1Rn90QghsFHpwdtVe4Tz1oTcEFa2vq5WSEZMKEcj7roPFq7nVdoN8VD2GYDI380R7iEXluYugTFGL+JcFW5zczCOVuK3sl8FhvtjQgb8gcJGsj6rJp4eScA+czX5EjVt2ARQsbJJNZbTskOeX0yv0cboWbiD5j9vJxxuVqjNXdrCB1PcbHiWVJVEChdn1guu/BoV3XSYS4DFMjf6Gx2taJhB6MScJ0dUmk=',
        'Connection': 'keep-alive',
        'Content-Length': '129',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'BIDUPSID=0FF5FE8984D9413B6C2EB0B3FC4F9D43; PSTM=1663117294; BAIDUID=0FF5FE8984D9413BC40DD8C95A533730:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=DFTSnE4VHVKLUxHS1ZpWjlnYks0NGR2c3RwcG1WbnhqZjRIU0xCY2xGZDdkR0pqSVFBQUFBJCQAAAAAAAAAAAEAAAAPt5c4v8mwrrXEYWppYW5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHvnOmN75zpjc; BDUSS_BFESS=DFTSnE4VHVKLUxHS1ZpWjlnYks0NGR2c3RwcG1WbnhqZjRIU0xCY2xGZDdkR0pqSVFBQUFBJCQAAAAAAAAAAAEAAAAPt5c4v8mwrrXEYWppYW5jb20AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHvnOmN75zpjc; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36556_37515_37768_37841_34813_37823_37760_37852_26350_22158; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=6; BAIDUID_BFESS=0FF5FE8984D9413BC40DD8C95A533730:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1668392967,1668758362,1669682028,1669692563; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1669692563; ab_sr=1.0.1_MDYzNmExNzlkODA1YzQ0OTI0ODc0MzgyYmExNmEzYThmMzk2NmViY2I5NzYyYWUzOTJlYmI3MDE1MDdlN2ZiZTI2ZGJiNTJjOTYyNTEwOTI4ODViZjE4MzlhMmE2NGZiYWVhYjU5NDg1OTI4MjdkMGRlNDFjMTU0YTRjY2FlYWQzYmE3MTU3NWM3NDI1MzNkYjNiZjkzNWM4NjE4Zjc2ZjlmNmQwYzYxYjNmMzNlZGUyNjE5MjkyMGFlNWI2MTc3',
        'Host': 'fanyi.baidu.com',
        'Origin': 'https://fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=1&keyfrom=baidu&smartresult=dict&lang=auto2zh',
        'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
        'X-Requested-With': 'XMLHttpRequest'
    }

    url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

    # 方法一：
    '''
    # 编译js
    js_obj = execjs.compile(open('./baidufanyi.js', 'r', encoding='utf-8').read())

    # 实用编译后的代码块call函数调用js文件中的hello_word函数
    sign = js_obj.call('f', word)  # "日本“的sign = 446766.143903
    # print(sign)
    '''

    # 方法二
    with open(r'./baidufanyi.js', 'r', encoding="utf-8") as f:    # /baidufanyi.js表示js文件
        jscode = f.read()
    js_obj = execjs.compile(jscode)     # 编译js文件
    sign = js_obj.call('f', word)    # f表示你要调用的js函数,word表示你传的参数
    print(sign)

    data = {
        'from': 'zh',
        'to': 'en',
        # 'from': 'en',
        # 'to': 'zh',
        'query': word,
        'transtype': 'enter',
        'simple_means_flag': 3,
        'sign': sign,
        'token': '18ac5ef61aef6cfce123876e67914c87',
        'domain': 'common'
    }

    resp = requests.post(url=url, headers=headers, data=data).json()
    print(resp["trans_result"]["data"][0]["dst"])
