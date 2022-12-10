'''
V1.1
    创建游戏窗口，循环移动

'''


import pygame
import random


VERSION = 'V1.01'
COLOR_BLACK = pygame.Color(0, 0, 0)
WIN_WIDTH = 1024
WIN_HEIGHT = 400
clock = pygame.time.Clock()

class MainGame():
    # 游戏窗口
    window = None
    bg = None
    map1_left = 0
    map2_left = 2048

    def __init__(self):
        pass

    def startGame(self):
        # 初始化游戏
        pygame.display.init()
        # 创建窗口
        MainGame.window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        # 设置游戏标题
        pygame.display.set_caption(f'跑酷{VERSION}')
        # 让窗口持续刷新
        while True:
            # 给窗口填充颜色
            self.window.fill(COLOR_BLACK)
            MainGame.bg = BackGround()
            MainGame.bg.displayBackGround(MainGame.map1_left)
            MainGame.bg.displayBackGround(MainGame.map2_left)
            MainGame.map1_left -= 4
            MainGame.map2_left -= 4
            if MainGame.map1_left <= -2048:
                MainGame.map1_left = WIN_WIDTH
            if MainGame.map2_left <= -2048:
                MainGame.map2_left = WIN_WIDTH
            self.getEvent()
            # 刷新窗口
            clock.tick(60)
            pygame.display.update()

    # 结束游戏方法
    def endGame(self):
        print("Game Over！！！")
        exit()

    # 事件响应
    def getEvent(self):
        # 获取事件列表
        eventList = pygame.event.get()
        # 遍历事件列表，处理事件
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()


class Player():
    def __init__(self):
        pass

    def jump(self):
        pass

    def desplay(self):
        pass


class Obstacle():
    def __init__(self):
        pass

    def display(self):
        pass

    def move(self):
        pass


class BackGround():
    def __init__(self):
        self.image = pygame.image.load('素材/map1.png')
        self.left = 0

    # 背景图循环展示
    def displayBackGround(self, left):
        MainGame.window.blit(self.image, (left, 0))


MainGame().startGame()