'''
谷歌webdriver下载地址：https://registry.npmmirror.com/binary.html?path=chromedriver/
酷狗音乐数据包地址：https://wwwapi.kugou.com/yy/index.php
    请求参数：
        data={
            r:
            callback:
            hash:
            dfid:
            appid:
            mid:
            platid:
            album_id:
            _:
        }
            pageurl: https://wwwapi.kugou.com/yy/index.php
            jsurl:
            jsurl2:
            ifameurl:
            uid: 0
            resurls: http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion=461746,http://js.tongji.linezing.com/1068373/tongji.js
            htype:
            resend: 0
            content:
            ispackage: 0
            ver: 0
            platform: web
'''
import requests
from tkinter import *

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class main:
    def __init__(self):
        self.mu_name_list = [1, 2, 3, 4]
        self.num = 0

        self.win = Tk()
        self.win.title('酷狗音乐下载器')
        self.win.geometry('350x600+700+20')

        # # 实例化浏览器，并访问酷狗
        # web = Chrome()

        # 无头参数设置
        self.opt = Options()
        self.opt.add_argument("--headless")  # 无头
        self.opt.add_argument('--disable-gpu')

        self.web = Chrome(options=self.opt)

        self.entry = Entry(self.win, width=39)
        self.search_bt = Button(self.win, text='搜索', width=10, command=self.search_bt_click)
        self.download_bt = Button(self.win, text='下载', width=50, command=self.download_bt_click)
        self.lb = Listbox(self.win, selectmode=SINGLE, bg='white', width=51, height=100)
        self.entry.grid(row=0, )
        self.search_bt.grid(row=0, column=1)
        self.download_bt.grid(row=1, columnspan=2)
        self.lb.grid(row=3, rowspan=2, column=0, columnspan=3)

        self.win.mainloop()

    def search_bt_click(self):
        music_name = self.entry.get()
        print('你输入的歌曲/歌手是：', music_name)
        self.web.get(f'https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord={music_name}')
        self.mu_name_list = self.web.find_elements(By.XPATH, '/html/body/div[4]/div[1]/div[2]/ul[2]/li/div[1]/a')
        print('搜索到的内容为：', self.mu_name_list)

        music_name_list = []
        for elm in self.mu_name_list:
            # music_name_list.append(elm)
            print(elm.get_attribute('title'))
            music_name_list.append(elm.get_attribute('title'))

        for i, elm in enumerate(music_name_list):
            self.lb.insert(i, elm)

    def download_bt_click(self):
        self.num = self.lb.curselection()[0]
        self.download_music(self.num)

    def download_music(self, num):
        print('你要下载的歌曲编号是：', num+1)
        self.mu_name_list = self.web.find_elements(By.XPATH, '/html/body/div[4]/div[1]/div[2]/ul[2]/li/div[1]/a')
        # print(mu_name_list)

        self.mu_name_list[num].click()
        music_name = self.mu_name_list[num].get_attribute('title')

        # 获取弹出的窗口
        win_list = self.web.window_handles
        # print(win_list)
        self.web.switch_to.window(win_list[-1])

        # 在弹出的播放页面源代码中找到下载地址
        url = self.web.find_element(By.XPATH, '/html/body/div[1]/audio').get_attribute('src')

        print(url)

        # 发送请求，下载数据
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
        }
        resp = requests.get(url, headers)
        # print(resp)
        data = resp.content
        self.save_file(music_name, data)

    def save_file(self, music_name, data):
        # 保存数据
        with open(f'./music/{music_name}.mp3', 'wb') as f:
            f.write(data)
        print(music_name, '下载完成')
        self.web.quit()
        self.win.quit()

if __name__ == '__main__':
    main()


'''
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
'''
