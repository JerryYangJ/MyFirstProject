from urllib.request import urlopen
import json

url = "http://www.baidu.com/"
resp = urlopen(url)

# with open("mybaidu.html",mode="w",encoding="utf-8") as f:
#     f.write(resp.read().decode("utf-8"))
# print("over!")

print(resp.read().decode("utf-8"))