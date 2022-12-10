import requests
from lxml import etree


url = 'https://mp.weixin.qq.com/s?__biz=MzIwMDI1OTk3OA==&mid=2652462033&idx=4&sn=af21f03e870534a553415802c8e1191d&chksm=8d121b34ba6592225e9ef42a7dbb49f3c261571f11014caa5e0220604f3a6db993e06619d3a6&scene=27'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}

resp = requests.get(url=url, headers=headers)
# resp.encoding = "gbK"
resp = resp.text
# print(resp)
tree = etree.HTML(resp)
data = tree.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/p/span//text()')
data_text = ''.join(data)
# print(s)
with open('QC1.txt', 'a', encoding='utf-8') as f:
    for i in range(len(data)):
        f.write(data[i])
        f.write('\n')


