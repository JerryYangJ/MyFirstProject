"""
    @ display模块：窗体显示
        pygame.display.init        初始化display模块
        pygame.display.quit         结束display模块
        pygame.display.get_init     如果display模块已被初始化，则返回True
        pygame.display.set.mode     初始化一个准备显示的界面
        pygame.display.get_surface      获取当前surface对象
        pygame.display.flip         更新整个待显示的surface对象到屏幕上
        pygame.display.update       更新部分内容显示到屏幕上，如果没有参数，则与flip功能相同

    @ pygame.event.get():能够获取事件队列，使用for...in历遍事件，然后根据type属性判定事件类型
        event.type     事件类型
            pygame.QUIT     关闭pygame窗口事件
            pygame.KEYDOWN    表示键盘按下事件
            pygame.MOUSEBUTTONDOWN      表示鼠标安歇事件

    @ image模块
        load()方法： 加载图片，返回值是一个Surface对象，是用来代表图片的pygame对象，可以对一个Surface对象进行图画、变形、复制等各种操作。
                    实际上屏幕也是一个Surface对象，pygame.display.set_mode就返回了一个屏幕Surface对象。
        blit()方法：  将Surface对象画到screen Surface对象
        flip()方法：  更新整个待显示的Surface对象到屏幕上

    @ Surface对象常用方法：
        pygame.Surface.blit     将一个图像画到另一个图像上
        pygame.Surface.convert  转换图像的像素格式
        pygame.Surface.covert_alpha     转化图像的像素格式，包含alpha通道的转换
        pygame.Surface.fill     使用颜色填充Surface
        pygame.Surface.get_rect     获取Surface的矩形区域

"""


import sys
import pygame

pygame.init()
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
color = (0, 0, 0)

ball = pygame.image.load('ball.png')        # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域

speed = [1, 1]      # 设置移动的x轴、y轴距离
clock = pygame.time.Clock()     # 设置时钟
# 执行死循环，确保窗口一直显示
while True:
    clock.tick(120)          # 每秒执行次数（帧率）
    for event in pygame.event.get():        # 历遍所有事件
        if event.type == pygame.QUIT:       # 如果单击关闭窗口，则退出
            sys.exit()
    ballrect = ballrect.move(speed)         # 移动小球
    # 碰到左右边缘
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(color)                      # 填充颜色
    screen.blit(ball, ballrect)             # 将图片画到窗口上
    pygame.display.flip()                   # 更新全部显示



pygame.quit()   # 退出pygame