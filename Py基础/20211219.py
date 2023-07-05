#加载背景音乐
#播放背景音乐并设置循环播放

interval = 0

while True:
    if 用户是否点击了关闭按钮
        退出程序（break）
    interval += 1
    if interval ==50:
        interval = 0
    小飞机出现
    小飞机移动一个位置
    屏幕刷新
    if 用户鼠标产生移动
        我方飞机中心位置=用户鼠标位置
        屏幕刷新
    if 我方飞机与小飞机发生结束
        我方飞机爆炸，播放撞击音乐
        修改我方飞机图案
        打印“GAME OVER！”
        停止背景音乐，淡出