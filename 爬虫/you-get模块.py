# @Time :2022/8/31 11:29
# @Author : Jerry Y
# @File  : you-get模块.py
# @Info  :中文说明：https://github.com/soimort/you-get/wiki/%E4%B8%AD%E6%96%87%E8%AF%B4%E6%98%8E

'''
    you-get的参数
        you-get -i https://v.qq.com/x/cover/34rg8ntemeszdm4/j0613bozdsx.html
        you-get -i 视频的地址           :解析出地址下的视频信息
        you-get -o <path> 视频的地址    :要保存的地址，包含视频的网页url
        you-get -u 视频的地址           :解析视频的真实地址url
        you-get --json 视频的地址       :获取视频的json格式
        you-get --itag=18 'https://www.youtube.com/watch?v=jNQXAC9IVRw'     ：以MP4格式下载

    乱码问题的解决方法
    　　1.CMD窗口下输入：chcp 65001 #UTF-8字符集代码，默认GBK为936
    　　2.CMD窗口上方标题栏，属性--字体中，修改为TrueType 'Lucida Console'

    支持网站
网站	URL	视频?	图像?	音频?
YouTube	https://www.youtube.com/	✓
Twitter	https://twitter.com/	✓	✓
VK	http://vk.com/	✓
Vine	https://vine.co/	✓
Vimeo	https://vimeo.com/	✓
Vidto	http://vidto.me/	✓
Veoh	http://www.veoh.com/	✓
Tumblr	https://www.tumblr.com/	✓	✓	✓
TED	http://www.ted.com/	✓
SoundCloud	https://soundcloud.com/	 	 	✓
Pinterest	https://www.pinterest.com/	 	✓
MusicPlayOn	http://en.musicplayon.com/	✓
MTV81	http://www.mtv81.com/	✓
Mixcloud	https://www.mixcloud.com/	 	 	✓
Metacafe	http://www.metacafe.com/	✓
Magisto	http://www.magisto.com/	✓
Khan Academy	https://www.khanacademy.org/	✓
JPopsuki TV	http://www.jpopsuki.tv/	✓
Internet Archive	https://archive.org/	✓
Instagram	https://instagram.com/	✓	✓
Heavy Music Archive	http://www.heavy-music.ru/	 	 	✓
Google+	https://plus.google.com/	✓	✓
Freesound	http://www.freesound.org/	 	 	✓
Flickr	https://www.flickr.com/	✓	✓
Facebook	https://www.facebook.com/	✓
eHow	http://www.ehow.com/	✓
Dailymotion	http://www.dailymotion.com/	✓
CBS	http://www.cbs.com/	✓
Bandcamp	http://bandcamp.com/	 	 	✓
AliveThai	http://alive.in.th/	✓
interest.me	http://ch.interest.me/tvn	✓
755
ナナゴーゴー	http://7gogo.jp/	✓	✓
niconico
ニコニコ動画	http://www.nicovideo.jp/	✓
163
网易视频
网易云音乐	http://v.163.com/
http://music.163.com/	✓	 	✓
56网	http://www.56.com/	✓
AcFun	http://www.acfun.tv/	✓
Baidu
百度贴吧	http://tieba.baidu.com/	✓	✓
爆米花网	http://www.baomihua.com/	✓
bilibili
哔哩哔哩	http://www.bilibili.com/	✓
Dilidili	http://www.dilidili.com/	✓
豆瓣	http://www.douban.com/	 	 	✓
斗鱼	http://www.douyutv.com/	✓
凤凰视频	http://v.ifeng.com/	✓
风行网	http://www.fun.tv/	✓
iQIYI
爱奇艺	http://www.iqiyi.com/	✓
激动网	http://www.joy.cn/	✓
酷6网	http://www.ku6.com/	✓
酷狗音乐	http://www.kugou.com/	 	 	✓
酷我音乐	http://www.kuwo.cn/	 	 	✓
乐视网	http://www.letv.com/	✓
荔枝FM	http://www.lizhi.fm/	 	 	✓
秒拍	http://www.miaopai.com/	✓
MioMio弹幕网	http://www.miomio.tv/	✓
痞客邦	https://www.pixnet.net/	✓
PPTV聚力	http://www.pptv.com/	✓
齐鲁网	http://v.iqilu.com/	✓
QQ
腾讯视频	http://v.qq.com/	✓
阡陌视频	http://qianmo.com/	✓
Sina
新浪视频
微博秒拍视频	http://video.sina.com.cn/
http://video.weibo.com/	✓
Sohu
搜狐视频	http://tv.sohu.com/	✓
天天动听	http://www.dongting.com/	 	 	✓
Tudou
土豆	http://www.tudou.com/	✓
虾米	http://www.xiami.com/	 	 	✓
阳光卫视	http://www.isuntv.com/	✓
音悦Tai	http://www.yinyuetai.com/	✓
Youku
优酷	http://www.youku.com/	✓
战旗TV	http://www.zhanqi.tv/lives	✓
央视网	http://www.cntv.cn/	✓
'''
# import scrapy
# from scrapy import cmdline
#
# # 使用cmdline.execute方法执行命令，execute方法的参数是列表
# cmdline.execute('you-get -i https://v.qq.com/x/cover/34rg8ntemeszdm4/j0613bozdsx.html'.split())

import os

# os.system('you-get -i https://open.163.com/newview/movie/free?pid=REVJH4NHE&mid=WEVJH4P9P')
# os.system('you-get -u https://open.163.com/newview/movie/free?pid=REVJH4NHE&mid=WEVJH4P9P')
os.system('you-get -o https://www.bilibili.com/video/BV185411t7Ux/?spm_id_from=333.880.my_history.page.click&vd_source=927f6f12fc5e8e5f44d522566a9ead0e')