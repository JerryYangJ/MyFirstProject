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



'''
搜索歌曲API：http://s.music.qq.com/fcgi-bin/music_search_new_platform?t=0& amp;n={2}&aggr=1&cr=1&loginUin={3}&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqminiframe.json&needNewCode=0&p={1}&catZhida=0&remoteplace=sizer.newclient.next_song&w={0}
{0}=需要搜索的歌曲或歌手
{1}=查询的页码数
{2}=当前页的返回数量
{3}=默认为0,是登录的QQ号ID
例子：http://s.music.qq.com/fcgi-bin/music_search_new_platform?t=0& n=5&aggr=1&cr=1&loginUin=0&format=json& inCharset=GB2312&outCharset=utf-8&notice=0& platform=jqminiframe.json&needNewCode=0&p=1&catZhida=0& remoteplace=sizer.newclient.next_song&w=周杰伦
返回
{
    "code": 0,
    "data": {
        "keyword": "周杰伦",
        "priority": 0,
        "qc": [],
        "semantic": {
            "curnum": 0,
            "curpage": 1,
            "list": [],
            "totalnum": 0
        },
        "song": {
            "curnum": 15,
            "curpage": 1,
            "list": [
                {
                    "albumName_hilight": "哎呦，不错哦",
                    "chinesesinger": 0,
                    "docid": "8758666917101856462",
                    "f": "101369814|算什么男人|4558|周杰伦|852856|哎呦，不错哦|2496580|289|6|1|0|11580808|4632445|320000|0|31933476|32002118|6708265|6989683|0|001Js78a40BZU6|0025NhlN2yWrP4|001uqejs3d6EID|31|0",
                    "fiurl": "",
                    "fnote": 0,
                    "fsinger": "周杰伦",
                    "fsinger2": "",
                    "fsong": "算什么男人",
                    "grp": [],
                    "isupload": 0,
                    "isweiyun": 0,
                    "lyric": "",
                    "lyric_hilight": "",
                    "mv": "c0015vx9gdg",
                    "nt": 10000,
                    "only": 1,
                    "pubTime": 1419523200,
                    "pure": 0,
                    "singerMID": "0025NhlN2yWrP4",
                    "singerMID2": "",
                    "singerName2_hilight": "",
                    "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                    "singerid": 4558,
                    "singerid2": 0,
                    "songName_hilight": "算什么男人",
                    "t": 1,
                    "tag": 10,
                    "ver": 0
                },
                {
                    "albumName_hilight": "哎呦，不错哦",
                    "chinesesinger": 0,
                    "docid": "12455748783386394049",
                    "f": "101787870|手写的从前|4558|周杰伦|852856|哎呦，不错哦|2563780|297|6|1|0|11901591|4760759|320000|0|31919200|32299126|6686621|6881464|0|002u8ZOM4C7QF4|0025NhlN2yWrP4|001uqejs3d6EID|31|0",
                    "fiurl": "",
                    "fnote": 0,
                    "fsinger": "周杰伦",
                    "fsinger2": "",
                    "fsong": "手写的从前",
                    "grp": [
                        {
                            "albumName_hilight": "2015江苏卫视新年演唱会",
                            "chinesesinger": 0,
                            "docid": "8524459989778971468",
                            "f": "101803866|手写的从前|4558|周杰伦|929853|2015江苏卫视新年演唱会|2474194|287|3|1|0|0|4596097|128000|0|0|0|0|0|0|001cCPt60GRPUz|0025NhlN2yWrP4|002xOmp62kqSic|31|0",
                            "fiurl": "",
                            "fnote": 0,
                            "fsinger": "周杰伦",
                            "fsinger2": "",
                            "fsong": "手写的从前 (Live)",
                            "isupload": 0,
                            "isweiyun": 0,
                            "lyric": "",
                            "lyric_hilight": "",
                            "mv": "a0015etg641",
                            "nt": 10001,
                            "only": 0,
                            "pubTime": 1420041600,
                            "pure": 0,
                            "singerMID": "0025NhlN2yWrP4",
                            "singerMID2": "",
                            "singerName2_hilight": "",
                            "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                            "singerid": 4558,
                            "singerid2": 0,
                            "songName_hilight": "手写的从前 (Live)",
                            "t": 1,
                            "tag": 0,
                            "ver": 0
                        }
                    ],
                    "isupload": 0,
                    "isweiyun": 0,
                    "lyric": "优酸乳为爱告白 广告曲",
                    "lyric_hilight": "优酸乳为爱告白 广告曲",
                    "mv": "k0015ms0ov0",
                    "nt": 10001,
                    "only": 1,
                    "pubTime": 1419523200,
                    "pure": 0,
                    "singerMID": "0025NhlN2yWrP4",
                    "singerMID2": "",
                    "singerName2_hilight": "",
                    "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                    "singerid": 4558,
                    "singerid2": 0,
                    "songName_hilight": "手写的从前",
                    "t": 1,
                    "tag": 10,
                    "ver": 0
                },
                {
                    "albumName_hilight": "我很忙",
                    "chinesesinger": 0,
                    "docid": "4953153690890266244",
                    "f": "410316|青花瓷|4558|周杰伦|33021|我很忙|1942555|239|8|1|0|9573872|3836490|320000|0|25541938|26237796|5414428|5617369|0|002qU5aY3Qu24y|0025NhlN2yWrP4|002eFUFm2XYZ7z|31|0",
                    "fiurl": "",
                    "fnote": 0,
                    "fsinger": "周杰伦",
                    "fsinger2": "",
                    "fsong": "青花瓷",
                    "grp": [
                        {
                            "albumName_hilight": "K情歌10",
                            "chinesesinger": 0,
                            "docid": "11254040215489699229",
                            "f": "4758498|青花瓷|4558|周杰伦|423011|K情歌10|2045366|237|1|1|0|0|3799447|128000|0|0|0|0|0|0|0034axGS2MI3sT|0025NhlN2yWrP4|002GJDhP0ZluDv|31|0",
                            "fiurl": "",
                            "fnote": 0,
                            "fsinger": "周杰伦",
                            "fsinger2": "",
                            "fsong": "青花瓷",
                            "isupload": 0,
                            "isweiyun": 0,
                            "lyric": "",
                            "lyric_hilight": "",
                            "mv": "l00131om505",
                            "nt": 10002,
                            "only": 0,
                            "pubTime": 1361462400,
                            "pure": 0,
                            "singerMID": "0025NhlN2yWrP4",
                            "singerMID2": "",
                            "singerName2_hilight": "",
                            "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                            "singerid": 4558,
                            "singerid2": 0,
                            "songName_hilight": "青花瓷",
                            "t": 1,
                            "tag": 0,
                            "ver": 0
                        },
                        {
                            "albumName_hilight": "热搜铃声",
                            "chinesesinger": 0,
                            "docid": "2997797877615103176",
                            "f": "101835716|青花瓷 (铃声)|4558|周杰伦|881348|热搜铃声|326994|37|8|1|0|1512185|605005|320000|0|4625595|4683771|921951|952005|0|004bOIwA0347Lp|0025NhlN2yWrP4|001S6jc81P4OvC|31|0",
                            "fiurl": "",
                            "fnote": 0,
                            "fsinger": "周杰伦",
                            "fsinger2": "",
                            "fsong": "青花瓷 (铃声)",
                            "isupload": 0,
                            "isweiyun": 0,
                            "lyric": "",
                            "lyric_hilight": "",
                            "mv": "",
                            "nt": 10002,
                            "only": 0,
                            "pubTime": 1420041600,
                            "pure": 0,
                            "singerMID": "0025NhlN2yWrP4",
                            "singerMID2": "",
                            "singerName2_hilight": "",
                            "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                            "singerid": 4558,
                            "singerid2": 0,
                            "songName_hilight": "青花瓷 (铃声)",
                            "t": 1,
                            "tag": 0,
                            "ver": 0
                        }
                    ],
                    "isupload": 0,
                    "isweiyun": 0,
                    "lyric": "",
                    "lyric_hilight": "",
                    "mv": "l00131om505",
                    "nt": 10002,
                    "only": 1,
                    "pubTime": 1193932800,
                    "pure": 0,
                    "singerMID": "0025NhlN2yWrP4",
                    "singerMID2": "",
                    "singerName2_hilight": "",
                    "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                    "singerid": 4558,
                    "singerid2": 0,
                    "songName_hilight": "青花瓷",
                    "t": 1,
                    "tag": 0,
                    "ver": 0
                },
                {
                    "albumName_hilight": "寻找<span class="c_tx_highlight">周杰伦</span>",
                    "chinesesinger": 0,
                    "docid": "10191134707667032736",
                    "f": "97783|断了的弦|4558|周杰伦|8221|寻找周杰伦|2378573|293|10|1|0|11744124|4696154|320000|0|31218341|32737193|6808158|7168784|0|003nK1U41u00q1|0025NhlN2yWrP4|001BGzMs369FzU|31|0",
                    "fiurl": "",
                    "fnote": 0,
                    "fsinger": "周杰伦",
                    "fsinger2": "",
                    "fsong": "断了的弦 (伴奏)",
                    "grp": [
                        {
                            "albumName_hilight": "寻找<span class="c_tx_highlight">周杰伦</span>",
                            "chinesesinger": 0,
                            "docid": "2690403057583679707",
                            "f": "97782|断了的弦|4558|周杰伦|8221|寻找周杰伦|2411617|297|9|1|0|11895634|4763445|320000|0|31653329|33029764|6553270|6984540|0|003ZdxP61ClQZ5|0025NhlN2yWrP4|001BGzMs369FzU|31|0",
                            "fiurl": "",
                            "fnote": 0,
                            "fsinger": "周杰伦",
                            "fsinger2": "",
                            "fsong": "断了的弦",
                            "isupload": 0,
                            "isweiyun": 0,
                            "lyric": "电影《寻找周杰伦》插曲",
                            "lyric_hilight": "电影《寻找<span class="c_tx_highlight">周杰伦</span>》插曲",
                            "mv": "r0013wcyzl4",
                            "nt": 10003,
                            "only": 0,
                            "pubTime": 1067616000,
                            "pure": 0,
                            "singerMID": "0025NhlN2yWrP4",
                            "singerMID2": "",
                            "singerName2_hilight": "",
                            "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                            "singerid": 4558,
                            "singerid2": 0,
                            "songName_hilight": "断了的弦",
                            "t": 1,
                            "tag": 0,
                            "ver": 0
                        },
                        {
                            "albumName_hilight": "<span class="c_tx_highlight">周杰伦</span> 2004 无与伦比 演唱会 Live CD",
                            "chinesesinger": 0,
                            "docid": "9281317214309150225",
                            "f": "4962992|断了的弦|4558|周杰伦|14323|周杰伦 2004 无与伦比 演唱会 Live CD|2503008|290|3|1|0|11615325|4646274|320000|0|35608020|35843959|6682152|7228609|0|0006yaTm0WDI7M|0025NhlN2yWrP4|0032ezFm3F53yO|31|0",
                            "fiurl": "",
                            "fnote": 0,
                            "fsinger": "周杰伦",
                            "fsinger2": "",
                            "fsong": "断了的弦 (Live)",
                            "isupload": 0,
                            "isweiyun": 0,
                            "lyric": "",
                            "lyric_hilight": "",
                            "mv": "",
                            "nt": 10003,
                            "only": 0,
                            "pubTime": 1106150400,
                            "pure": 0,
                            "singerMID": "0025NhlN2yWrP4",
                            "singerMID2": "",
                            "singerName2_hilight": "",
                            "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                            "singerid": 4558,
                            "singerid2": 0,
                            "songName_hilight": "断了的弦 (Live)",
                            "t": 1,
                            "tag": 0,
                            "ver": 0
                        }
                    ],
                    "isupload": 0,
                    "isweiyun": 0,
                    "lyric": "",
                    "lyric_hilight": "",
                    "mv": "",
                    "nt": 10003,
                    "only": 1,
                    "pubTime": 1067616000,
                    "pure": 0,
                    "singerMID": "0025NhlN2yWrP4",
                    "singerMID2": "",
                    "singerName2_hilight": "",
                    "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                    "singerid": 4558,
                    "singerid2": 0,
                    "songName_hilight": "断了的弦 (伴奏)",
                    "t": 1,
                    "tag": 10,
                    "ver": 0
                },
                {
                    "albumName_hilight": "Jay",
                    "chinesesinger": 0,
                    "docid": "14303915167107409415",
                    "f": "97758|龙卷风|4558|周杰伦|8218|Jay|2033113|250|5|1|0|10037805|4016134|320000|0|26976920|27794719|5309494|5960922|0|002l8JN71d2Dxy|0025NhlN2yWrP4|000f01724fd7TH|31|0",
                    "fiurl": "",
                    "fnote": 0,
                    "fsinger": "周杰伦",
                    "fsinger2": "",
                    "fsong": "龙卷风",
                    "grp": [
                        {
                            "albumName_hilight": "The Era 2010 超时代演唱会",
                            "chinesesinger": 0,
                            "docid": "11830165131099900276",
                            "f": "4829324|龙卷风|4558|周杰伦|67340|The Era 2010 超时代演唱会|2147768|249|10|1|0|9964201|3985858|320000|0|31274215|31521569|5652283|6136785|0|001H8Gae45ikHR|0025NhlN2yWrP4|002o2a5G46ETLr|31|0",
                            "fiurl": "",
                            "fnote": 0,
                            "fsinger": "周杰伦",
                            "fsinger2": "",
                            "fsong": "龙卷风 (Live)",
                            "isupload": 0,
                            "isweiyun": 0,
                            "lyric": "",
                            "lyric_hilight": "",
                            "mv": "X0010KChPCn",
                            "nt": 10004,
                            "only": 0,
                            "pubTime": 1295884800,
                            "pure": 0,
                            "singerMID": "0025NhlN2yWrP4",
                            "singerMID2": "",
                            "singerName2_hilight": "",
                            "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                            "singerid": 4558,
                            "singerid2": 0,
                            "songName_hilight": "龙卷风 (Live)",
                            "t": 1,
                            "tag": 0,
                            "ver": 0
                        },
                        {
                            "albumName_hilight": "<span class="c_tx_highlight">周杰伦</span> 2004 无与伦比 演唱会 Live CD",
                            "chinesesinger": 0,
                            "docid": "13224632523111011719",
                            "f": "4962978|龙卷风|4558|周杰伦|14323|周杰伦 2004 无与伦比 演唱会 Live CD|2141406|248|3|1|0|9935127|3974193|320000|0|30864029|31432703|5698109|6273651|0|000vm0CC2N5DvK|0025NhlN2yWrP4|0032ezFm3F53yO|31|0",
                            "fiurl": "",
                            "fnote": 0,
                            "fsinger": "周杰伦",
                            "fsinger2": "",
                            "fsong": "龙卷风 (Live)",
                            "isupload": 0,
                            "isweiyun": 0,
                            "lyric": "",
                            "lyric_hilight": "",
                            "mv": "",
                            "nt": 10004,
                            "only": 0,
                            "pubTime": 1106150400,
                            "pure": 0,
                            "singerMID": "0025NhlN2yWrP4",
                            "singerMID2": "",
                            "singerName2_hilight": "",
                            "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                            "singerid": 4558,
                            "singerid2": 0,
                            "songName_hilight": "龙卷风 (Live)",
                            "t": 1,
                            "tag": 0,
                            "ver": 0
                        },
                        {
                            "albumName_hilight": "The One演唱会",
                            "chinesesinger": 0,
                            "docid": "12140579362073679756",
                            "f": "7098053|龙卷风|4558|周杰伦|14320|The One演唱会|2144584|248|10|1|0|9946591|3978761|320000|0|30048676|30509084|5270411|6062959|0|002RY0aC4612wn|0025NhlN2yWrP4|001O06fF2b3W8P|31|0",
                            "fiurl": "",
                            "fnote": 0,
                            "fsinger": "周杰伦",
                            "fsinger2": "",
                            "fsong": "龙卷风 (Live)",
                            "isupload": 0,
                            "isweiyun": 0,
                            "lyric": "",
                            "lyric_hilight": "",
                            "mv": "",
                            "nt": 10004,
                            "only": 0,
                            "pubTime": 1033401600,
                            "pure": 0,
                            "singerMID": "0025NhlN2yWrP4",
                            "singerMID2": "",
                            "singerName2_hilight": "",
                            "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                            "singerid": 4558,
                            "singerid2": 0,
                            "songName_hilight": "龙卷风 (Live)",
                            "t": 1,
                            "tag": 0,
                            "ver": 0
                        },
                        {
                            "albumName_hilight": "Fantasy Show香港演唱会",
                            "chinesesinger": 0,
                            "docid": "7847914747533822478",
                            "f": "162379|龙卷风|4558|周杰伦|14319|Fantasy Show香港演唱会|2141879|263|4|1|0|0|4210067|0|0|0|0|0|0|0|001wJfUe4IGByO|0025NhlN2yWrP4|00474nNC0yEs3T|31|0",
                            "fiurl": "",
                            "fnote": 0,
                            "fsinger": "周杰伦",
                            "fsinger2": "",
                            "fsong": "龙卷风 (Live)",
                            "isupload": 0,
                            "isweiyun": 0,
                            "lyric": "",
                            "lyric_hilight": "",
                            "mv": "",
                            "nt": 10004,
                            "only": 0,
                            "pubTime": 1004889600,
                            "pure": 0,
                            "singerMID": "0025NhlN2yWrP4",
                            "singerMID2": "",
                            "singerName2_hilight": "",
                            "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                            "singerid": 4558,
                            "singerid2": 0,
                            "songName_hilight": "龙卷风 (Live)",
                            "t": 1,
                            "tag": 0,
                            "ver": 0
                        },
                        {
                            "albumName_hilight": "热搜铃声",
                            "chinesesinger": 0,
                            "docid": "10082662556977192226",
                            "f": "101835715|龙卷风 (铃声)|4558|周杰伦|881348|热搜铃声|282194|32|8|1|0|1299026|519585|320000|0|4220863|4221506|721369|812585|0|0004RoQz4B6efJ|0025NhlN2yWrP4|001S6jc81P4OvC|31|0",
                            "fiurl": "",
                            "fnote": 0,
                            "fsinger": "周杰伦",
                            "fsinger2": "",
                            "fsong": "龙卷风 (铃声)",
                            "isupload": 0,
                            "isweiyun": 0,
                            "lyric": "",
                            "lyric_hilight": "",
                            "mv": "",
                            "nt": 10004,
                            "only": 0,
                            "pubTime": 1420041600,
                            "pure": 0,
                            "singerMID": "0025NhlN2yWrP4",
                            "singerMID2": "",
                            "singerName2_hilight": "",
                            "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                            "singerid": 4558,
                            "singerid2": 0,
                            "songName_hilight": "龙卷风 (铃声)",
                            "t": 1,
                            "tag": 0,
                            "ver": 0
                        }
                    ],
                    "isupload": 0,
                    "isweiyun": 0,
                    "lyric": "",
                    "lyric_hilight": "",
                    "mv": "X0010KChPCn",
                    "nt": 10004,
                    "only": 1,
                    "pubTime": 973526400,
                    "pure": 0,
                    "singerMID": "0025NhlN2yWrP4",
                    "singerMID2": "",
                    "singerName2_hilight": "",
                    "singerName_hilight": "<span class="c_tx_highlight">周杰伦</span>",
                    "singerid": 4558,
                    "singerid2": 0,
                    "songName_hilight": "龙卷风",
                    "t": 1,
                    "tag": 0,
                    "ver": 0
                }
            ],
            "totalnum": 389
        },
        "totaltime": 0.00001,
        "zhida": {
            "chinesesinger": 0,
            "type": 0
        }
    },
    "message": "",
    "notice": "",
    "subcode": 0,
    "time": 1423298505,
    "tips": ""
}
分析json格式，歌曲名称，歌手，专辑，还有其中的f的属性
"f": "101369814|算什么男人|4558|周杰伦|852856|哎呦，不错哦|2496580|289|6|1|0|11580808|4632445|320000|0|31933476|32002118|6708265|6989683|0|001Js78a40BZU6|0025NhlN2yWrP4|001uqejs3d6EID|31|0"
id=001Js78a40BZU6
img=001uqejs3d6EID
lrc=101369814
这些ID在下面的API中会有用的

获取播放key：http://base.music.qq.com/fcgi-bin /fcg_musicexpress.fcg?json=3&loginUin={0}&format=jsonp&inCharset=GB2312&outCharset=GB2312&notice=0&platform=yqq&needNewCode=0
{0}=默认为0,是登录的QQ号ID

返回
jsonCallback({"code":0,"sip"["http://ws.stream.qqmusic.qq.com/","http://cc.stream.qqmusic.qq.com/","http://124.14.15.19/streamoc.music.tc.qq.com/"],"key":"6BFDD0DFE8A88C65E5D7942967AE84A1F7BC2A96A9120C15A5032483EA5D0659"});
key=6BFDD0DFE8A88C65E5D7942967AE84A1F7BC2A96A9120C15A5032483EA5D0659

播放歌曲API：http://cc.stream.qqmusic.qq.com/C200{0}.m4a?vkey={1}&fromtag=0
{0}=上面取到的ID
{1}=上面取到的KEY

例子：http://cc.stream.qqmusic.qq.com /C200001Js78a40BZU6.m4a?vkey=6BFDD0DFE8A88C65E5D7942967AE84A1F7BC2A96A9120C15A5032483EA5D0659&fromtag=0

歌曲图片API：http://imgcache.qq.com/music/photo/mid_album_90/{1}/{2}/{0}.jpg
{0}=上面取到的Img
{1]=上面取到的Img的倒数第二个字符
{2}=上面取到的Img的最后一个字符

例子：http://imgcache.qq.com/music/photo/mid_album_90/I/D/001uqejs3d6EID.jpg

歌词API：http://music.qq.com/miniportal/static/lyric/{1}/{0}.xml
{0}=上面取到的Lrc
{1}=上面取到的Lrc%100

例子：http://music.qq.com/miniportal/static/lyric/14/101369814.xml
这个LRC有时会失效的
'''
