import requests
from lxml import etree

# 拿到源代码
url = "https://www.wenxm.cn/ziwopingjia/604274.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "Accept-Encoding": "gzip"
}
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'

# 网站响应数据类型为gzip,需要进行转码
page_content = resp.text.encode('gbk', 'ignore').decode('gbk')
# print(page_content)

# 用xpath解析提取数据
tree = etree.HTML(page_content)
result = tree.xpath('//p[@style="text-indent: 2em; text-align: left;"]/text()')

# 合并字符串（列表）
result_text = '\n'.join(result)

# 输出
print(result_text)
