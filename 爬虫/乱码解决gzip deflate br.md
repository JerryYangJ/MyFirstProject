目录 1、问题如下2、解决问题

1、问题如下   
乱码bug集1前提：resp.encoding编码与网页源码编码一致；本例编码为’utf-8’；
直接输出reponse.text会报异常：
```python
UnicodeEncodeError: ‘gbk’ codec can’t encode character ‘\ufffd’ in position 0: illegal multibyte sequence 
headers = { 'accept': "text/html, application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,v=b3", 
            'accept-Encoding': "gzip, deflate, br", 
            'accept-Language': "zh-CN,zh;q=0.9", 
            'connection': "close", 
            'Upgrade-Insecure-Requests': '1', 
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36", 
            }

resp = requests.get(url, headers=headers, proxies=proxy, timeout=20)
resp.encoding = 'utf-8'
print(resp.text)
```

修改print(resp.text)，出现如下乱码   
```python
headers = { 'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,v=b3", 
            'accept-Encoding': "gzip, deflate, br", 
            'accept-Language': "zh-CN,zh;q=0.9", 
            'connection': "close", 
            'Upgrade-Insecure-Requests': '1', 
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36", 
            }

resp = requests.get(url, headers=headers, proxies=proxy, timeout=20)
resp.encoding = 'utf-8'
print(resp.text.encode('gbk', 'ignore').decode('gbk'))
```
2、解决问题   
将 ‘accept-Encoding’: "gzip, deflate, br"里面的br去掉即可，或者这一行直接注释掉  
```python
headers = { 'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,v=b3", 
            'accept-Encoding': "gzip, deflate", 
            'accept-Language': "zh-CN,zh;q=0.9", 
            'connection': "close", 
            'Upgrade-Insecure-Requests': '1', 
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36", 
            }
resp = requests.get(url, headers=headers, proxies=proxy, timeout=20)
resp.encoding = 'utf-8'
print(resp.text.encode('gbk', 'ignore').decode('gbk'))

```