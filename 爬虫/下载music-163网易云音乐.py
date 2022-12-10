import time
import requests

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

music_name = input("请输入你要搜索的歌曲名称：")
# 实例化浏览器，并访问网易云音乐网站
web = Chrome()
web.get('https://music.163.com/#/search')

# 定位歌曲歌曲搜索框
web.switch_to.frame('contentFrame')
input = web.find_element(By.ID, 'm-search-input')
input.send_keys(music_name)
input.send_keys(Keys.ENTER)

# 等待3秒
time.sleep(3)

# print(web.page_source)

# 解析网页源代码，提取name,id
# /html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span
mu_name = web.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/a[1]/b/span').text
mu_id = web.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/a[1]').get_attribute('href')
mu_id = mu_id.split('=')[-1]
print(mu_name, mu_id)
# 下载数据
# mu_id = '1901371647'   # 孤勇者ID=1901371647
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
download_url = f'http://music.163.com/song/media/outer/url?id={mu_id}'
resp = requests.get(download_url, headers)
data = resp.content

# 保存数据
with open(f'./music/{mu_name}.mp3', 'wb') as f:
    f.write(data)
print(mu_name, '下载完成')
