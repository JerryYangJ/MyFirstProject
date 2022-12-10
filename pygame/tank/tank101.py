'''
V1.01
新增功能
创建游戏窗口

'''

import pygame


VESSION = 'V1.01'
COLOR_BLACK = pygame.Color(0, 0, 0)


class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800

    def __init__(self):
        pass

    # 开始游戏方法
    def startGame(self):
        # 初始化游戏
        pygame.display.init()
        # 创建窗口，加载窗口
        self.window = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        # 设置标题
        pygame.display.set_caption('坦克大战'+VESSION)
        # 让窗口持续刷新
        while True:
            # 给窗口填充颜色
            self.window.fill(COLOR_BLACK)
            pygame.display.update()



    # 结束游戏方法
    def endGame(self):
        print('游戏结束')
        exit()


class Tank():
    def __init__(self):
        pass

    # 坦克移动方法
    def move(self):
        pass

    # 坦克射击方法
    def shot(self):
        pass

    # 坦克显示方法
    def displayTank(self):
        pass


class MyTank(Tank):
    def __init__(self):
        pass


class EnemyTank(Tank):
    def __init__(self):
        pass


class Bullet():
    def __init__(self):
        pass

    # 子弹移动方法
    def move(self):
        pass

    # 子弹显示方法
    def displayBullet(self):
        pass


class Explode():
    def __init__(self):
        pass

    # 爆炸显示方法
    def displayExplode(self):
        pass


class wall():
    def __init__(self):
        pass

    def displayWall(self):
        pass


class Music():
    def __init__(self):
        pass

    # 音乐播放方法
    def play(self):
        pass


MainGame().startGame()
