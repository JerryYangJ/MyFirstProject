import requests
from lxml import etree


url = 'http://www.ts16949-sh.com/web/qc.asp#1'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}

resp = requests.get(url=url, headers=headers)
resp.encoding = "gbK"
resp = resp.text
# print(resp)
tree = etree.HTML(resp)
data = tree.xpath('/html//tr/td[3]/table//text()')
data_text = ''.join(data)
data_text.replace(f'/r', '')

print(data_text)
# with open('QC.txt', 'w', encoding='utf-8') as f:
#     f.write(data_text)


