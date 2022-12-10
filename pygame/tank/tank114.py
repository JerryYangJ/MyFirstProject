'''
V1.14
新增功能
    1.子弹打中墙壁时消除子弹：
    2.解决我方坦克可以无限发射子弹的情况，最多只能同时存在3发子弹

'''
import os
import random
import time

import pygame

VERSION = 'V1.14'
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_RED = pygame.Color(255, 0, 0)


class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    # 创建我方坦克
    TANK_P1 = None
    # 敌方坦克列表
    EnemyTank_list = []
    # 要创建的敌方坦克的数量
    EnemyTank_count = 5
    # 存储我方子弹的列表
    Bullet_list = []

    def __init__(self):
        pass

    # 开始游戏方法
    def startGame(self):
        # 初始化游戏
        pygame.display.init()
        # 创建窗口，加载窗口
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 创建我方坦克
        MainGame.TANK_P1 = Tank(350, 450)
        # 创建敌方坦克
        self.creatEnemyTank()
        # 设置标题
        pygame.display.set_caption('坦克大战' + VERSION)
        # 创建文字画布
        textsurface = self.getTextSurface('剩下的敌方坦克数量为%d辆' % len(MainGame.EnemyTank_list))
        # 让窗口持续刷新
        while True:
            # 给窗口填充颜色
            self.window.fill(COLOR_BLACK)
            # 获取事件
            self.getEvent()
            # 将文字画布blit到窗口中
            self.window.blit(textsurface, (10, 10))
            # 将玩家坦克加载到窗口中
            self.TANK_P1.displayTank()
            # 将敌方坦克加载到窗口中
            self.blitEnemyTank()
            # # 调用坦克的移动方法
            # MainGame.TANK_P1.move()
            # 根据坦克的开关状态调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
            time.sleep(0.02)
            # 调用渲染子弹列表的方法
            self.blitBullet()

            # 持续刷新
            pygame.display.update()

    # 创建敌方坦克方法
    def creatEnemyTank(self):
        top = 30
        speed = random.randint(3, 6)
        for i in range(MainGame.EnemyTank_count):
            left = random.randint(1, 7)
            eTank = EnemyTank(left * 100, top, speed)
            MainGame.EnemyTank_list.append(eTank)

    # 将敌方坦克加入到窗口方法
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            eTank.displayTank()
            # 敌方坦克移动
            eTank.randMove()

    # 将子弹加入到窗口方法
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            # 如果子弹还活着，则绘制子弹，否则从列表中删除子弹
            if bullet.live:
                bullet.displayBullet()
                # 让子弹移动
                bullet.move()
            else:
                MainGame.Bullet_list.remove(bullet)

    # 获取事件（鼠标、键盘事件）
    def getEvent(self):
        # 获取事件
        eventList = pygame.event.get()
        # 对事件进行判断处理
        for event in eventList:
            # 遍历事件列表，判断事件类型，处理
            if event.type == pygame.QUIT:
                self.endGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("坦克向左调头，移动")
                    # 修改坦克的方向
                    MainGame.TANK_P1.direction = 'L'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_RIGHT:
                    print("坦克向右调头，移动")
                    MainGame.TANK_P1.direction = 'R'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_UP:
                    print("坦克向上调头，移动")
                    MainGame.TANK_P1.direction = 'U'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_DOWN:
                    print("坦克向下调头，移动")
                    MainGame.TANK_P1.direction = 'D'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_SPACE:
                    print("坦克发射子弹")
                    if len(MainGame.Bullet_list) < 3:
                        # 产生一个子弹
                        m = Bullet(MainGame.TANK_P1)
                        # 将子弹加入到子弹列表
                        MainGame.Bullet_list.append(m)
                    else:
                        print('子弹数量不足')
                        print(f'当前子弹数量为：{len(MainGame.Bullet_list)}')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    # 修改坦克的移动开关
                    MainGame.TANK_P1.stop = True

    # 绘制文字
    def getTextSurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 获取系统支持的所有字体
        # fontlist = pygame.font.get_fonts()
        # print(fontlist)
        # 选中一个合适的字体
        font = pygame.font.SysFont('方正舒体', 18)
        textsurface = font.render(text, True, COLOR_RED)
        return textsurface

    # 结束游戏方法
    def endGame(self):
        print('游戏结束')
        exit()


class Tank():
    def __init__(self, left, top):
        self.images = {
            'U': pygame.image.load('素材/myTank-u.png'),
            'D': pygame.image.load('素材/myTank-d.png'),
            'L': pygame.image.load('素材/myTank-l.png'),
            'R': pygame.image.load('素材/myTank-r.png'),
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        # 坦克所在的区域
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = 5
        # 新增属性：坦克的移动开关
        self.stop = True

    # 坦克移动方法
    def move(self):
        if self.direction == 'L' and self.rect.left >= 0:
            self.rect.left -= self.speed
        elif self.direction == 'R' and self.rect.left <= MainGame.SCREEN_WIDTH - self.rect.width:
            self.rect.left += self.speed
        elif self.direction == 'U' and self.rect.top >= 0:
            self.rect.top -= self.speed
        elif self.direction == 'D' and self.rect.top <= MainGame.SCREEN_HEIGHT - self.rect.height:
            self.rect.top += self.speed

    # 坦克射击方法
    def shot(self):
        return Bullet(self)  # ??????????????????????

    # 坦克显示方法（将坦克绘制到窗口中，用blit())
    def displayTank(self):
        # 重新设置坦克图片
        self.image = self.images[self.direction]
        # 将坦克加入到窗口中
        MainGame.window.blit(self.image, self.rect)


class MyTank(Tank):
    def __init__(self):
        pass


class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        self.images = {
            'U': pygame.image.load('素材/坦克-u.png'),
            'D': pygame.image.load('素材/坦克-d.png'),
            'L': pygame.image.load('素材/坦克-l.png'),
            'R': pygame.image.load('素材/坦克-r.png'),
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        # 坦克所在的区域
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = speed
        # 新增属性：坦克的移动开关
        self.stop = True
        # 新增步数属性，控制坦克的随机移动
        self.step = 20

    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'

    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 20
        else:
            self.move()
            self.step -= 1

    def displayEnemytTank(self):
        super().displayTank()


class Bullet():
    def __init__(self, tank):
        # 图片
        self.image = pygame.image.load('素材/我方坦克子弹.png')
        # 方向
        self.direction = tank.direction
        # 位置
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.top
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        # 速度
        self.speed = 7
        # 增加子弹的状态，记录子弹是否碰撞
        self.live = True

    # 子弹移动方法
    def move(self):
        if self.direction == 'U' and self.rect.top > 0:
            self.rect.top -= self.speed
        elif self.direction == 'D' and self.rect.top < MainGame.SCREEN_HEIGHT - self.rect.height:
            self.rect.top += self.speed
        elif self.direction == 'L' and self.rect.left > 0:
            self.rect.left -= self.speed
        elif self.direction == 'R' and self.rect.left < MainGame.SCREEN_WIDTH - self.rect.width:
            self.rect.left += self.speed
        else:
            self.live = False
    # 子弹显示方法
    def displayBullet(self):
        MainGame.window.blit(self.image, self.rect)


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
