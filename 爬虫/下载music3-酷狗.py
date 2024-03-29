'''
酷狗音乐搜索接口：http://mobilecdn.kugou.com/api/v3/search/song?format=json&keyword=%E7%8E%8B%E5%8A%9B%E5%AE%8F&page=1&pagesize=20&showtype=1
    keyword：搜索的内容。
    page：搜索的页数
    pagesize：返回的数据量，填10就是返回1首歌曲的数据。
第二个是歌曲详细接口：http://www.kugou.com/yy/index.php?r=play/getdata""&hash=你需要填的&album_id=你需要填的&_=1497972864535
    hash和album_id都是第一个接口返回json解析出来的。
    通过该接口，我们可以得到歌曲播放地址，图片地址，歌词等等
'''



import requests

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

music_name = input("请输入你要搜索的歌曲或歌手名称：")
# 实例化浏览器，并访问酷狗
# web = Chrome()

# 无头参数设置
opt = Options()
opt.add_argument("--headless")  # 无头
opt.add_argument('--disable-gpu')

web = Chrome(options=opt)

web.get(f'https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord={music_name}')

# 解析网页源代码
mu_name_list = web.find_elements(By.XPATH, '/html/body/div[4]/div[1]/div[2]/ul[2]/li/div[1]/a')
i = 1
for elm in mu_name_list:
    print(i, elm.get_attribute('title'))
    i += 1

num = int(input('请输入要下载的歌曲编号：'))-1
mu_name_list[num].click()
music_name = mu_name_list[num].get_attribute('title')

# 获取弹出的窗口
win_list = web.window_handles
# print(win_list)
web.switch_to.window(win_list[-1])

# 在弹出的播放页面源代码中找到下载地址
url = web.find_element(By.XPATH, '/html/body/div[1]/audio').get_attribute('src')

print(url)

# 发送请求，下载数据
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
resp = requests.get(url, headers)
# print(resp)
data = resp.content

# 保存数据
with open(f'./music/{music_name}.mp3', 'wb') as f:
    f.write(data)
print(music_name, '下载完成')
