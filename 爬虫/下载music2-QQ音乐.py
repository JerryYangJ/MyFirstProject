import time
import requests

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
'''
    qq音乐：https://y.qq.com/portal/song/001faIUs4M2zna.html
    qq音乐搜索：https://y.qq.com/n/ryqq/search
    网易云音乐：http://music.163.com/#/m/song?id=5146554
    百度音乐1：http://music.taihe.com/song/950024
    百度音乐2：http://y.baidu.com/song/121280
    百度音乐3：http://y.taihe.com/song/121280
    虾米音乐：http://www.xiami.com/song/1770409076
    
'''
music_name = input("请输入你要搜索的歌曲名称：")
# 实例化浏览器，并访问网易云音乐网站
web = Chrome()
web.get('https://y.qq.com/n/ryqq/search')
time.sleep(3)           # 要×掉弹窗
close_bt = web.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/button/span')
close_bt.click()

time.sleep(3)
# 定位歌曲歌曲搜索框
input = web.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/input')
input.send_keys(music_name)


# 等待3秒
time.sleep(3)

# print(web.page_source)

# 解析网页源代码，提取href
mu_ch_url = web.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/ul/li[1]/a').get_attribute('href')
# print(mu_ch_url)

# web请求mu_ch_url,点击播放按钮，转到新window，抓取新window中的audio标签中的src属性值
web.execute_script('window.open()')
win_list = web.window_handles
# print(win_list)
web.switch_to.window(win_list[-1])

time.sleep(2)

web.get(mu_ch_url)

time.sleep(2)

play_bt = web.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div[3]/a[1]/span')
play_bt.click()

win_list = web.window_handles
# print(win_list)
web.switch_to.window(win_list[-1])

time.sleep(2)


download_url = web.find_element(By.XPATH, '/html/body/audio').get_attribute('src')
print(download_url)

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
resp = requests.get(download_url, headers)
data = resp.content

# 保存数据
with open(f'./music/{music_name}.mp3', 'wb') as f:
    f.write(data)
print(music_name, '下载完成')
