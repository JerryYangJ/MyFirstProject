import time

import requests
from lxml import etree

'''
采集的站点：

免费代理IP http://ip.yqie.com/ipproxy.htm
66免费代理网 http://www.66ip.cn/
89免费代理 http://www.89ip.cn/
无忧代理 http://www.data5u.com/
云代理 http://www.ip3366.net/
快代理 https://www.kuaidaili.com/free/
极速专享代理 http://www.superfastip.com/
HTTP代理IP https://www.xicidaili.com/wt/
小舒代理 http://www.xsdaili.com
西拉免费代理IP http://www.xiladaili.com/
小幻HTTP代理 https://ip.ihuan.me/
全网代理IP http://www.goubanjia.com/
飞龙代理IP http://www.feilongip.com/
'''

# 拿到源代码
url = "https://free.kuaidaili.com/free/inha/1/"
# url1 = "http://www.baidu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}
resp = requests.get(url, headers=headers)
page_content = resp.text

# print(page_content)

tree = etree.HTML(page_content)
# table = tree.xpath('/html/body/div/div[4]/div[2]/div[2]/div[2]/table/tbody')
IP_list = tree.xpath('//tr/td[1]/text()')
port_list = tree.xpath('//tr/td[2]/text()')
type_list = tree.xpath('//tr/td[4]/text()')
# print(IP_list, port_list, type_list)
url_list = []
ok_url_list = []
for type, IP, port in zip(type_list, IP_list, port_list):
    url = f'"{type.lower()}"' + ':' + f"'{IP}:{port}'"
    url1 = "//" + f'{IP}:{port}'
    # print(url1)

    # url1_list =[
    #     '//60.170.204.30:8060',
    #     '//120.220.220.95:8085',
    #     '//120.220.220.95:8085',
    #     '//223.96.90.216:8085',
    #     '//223.96.90.216:8085',
    #     '//47.113.90.161:83'
    # # ]
    # for url1 in url1_list:
    try:
        # ip_proxy = random.choice(http_ip)
        proxy_ip = {
            'http': url1,
            'https': url1,
        }
        print('使用代理的IP:', proxy_ip)
        response = requests.get("http://httpbin.org/ip", proxies=proxy_ip).text
        # print(response)
        # print('当前IP有效')
        ok_url_list.append(proxy_ip)
        time.sleep(2)
    except Exception as e:
        # print(e.args[0])
        # print('当前IP无效')
        continue

for proxy in ok_url_list:
    print(proxy)

"""
http_ip = [
    '118.163.13.200:8080',
    '222.223.182.66:8000',
    '51.158.186.242:8811',
    '171.37.79.129:9797',
    '139.255.123.194:4550'
]
"""
