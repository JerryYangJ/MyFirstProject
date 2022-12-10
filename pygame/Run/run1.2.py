'''
V1.2
    1，实现人物跑动
    2.创建随机障碍物，移动
    3.人物与障碍物碰撞检测
    4.添加背景音乐，循环播放
'''

import random

import pygame

VERSION = 'V1.2'
COLOR_BLACK = pygame.Color(0, 0, 0)
WIN_WIDTH = 1024
WIN_HEIGHT = 400
clock = pygame.time.Clock()
STEP = 5

player_image_list = [
    pygame.image.load('素材/run-1-1.png'),
    pygame.image.load('素材/run-2-1.png'),
    pygame.image.load('素材/run-3-1.png'),
    pygame.image.load('素材/run-4-1.png'),
    pygame.image.load('素材/run-5-1.png'),
    pygame.image.load('素材/run-6-1.png'),
    pygame.image.load('素材/run-7-1.png'),
    pygame.image.load('素材/run-8-1.png')
]

obstacle_image_list = [
    pygame.image.load('素材/YMM.png'),
    pygame.image.load('素材/YZX.png'),
    pygame.image.load('素材/YZH.png')
]


class MainGame():
    # 游戏窗口
    window = None
    map1_left = 0
    map2_left = 2048
    player_image_num = 0
    player = None
    obstacleList = []
    i = 0
    left = [random.randint(40, 100), random.randint(300, 400), random.randint(500, 800), random.randint(900, 1000)]


    def __init__(self):
        pass

    def startGame(self):
        # 初始化游戏
        pygame.display.init()
        # 创建窗口
        MainGame.window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        # 设置游戏标题
        pygame.display.set_caption(f'跑酷{VERSION}')
        # 创建player
        MainGame.player = Player()
        # 创建障碍物
        for i in range(0, 4):
            obstacle = Obstacle(MainGame.left[i])
            MainGame.obstacleList.append(obstacle)
        # 创建音乐对象
        music = Music('素材/奔跑吧兄弟a.mp3')
        # 播放音乐
        music.playMusic(-1)
        # 创建图片背景
        bg1 = BackGround(MainGame.map1_left)
        bg2 = BackGround(MainGame.map2_left)
        # 让窗口持续刷新
        while True:
            # 给窗口填充颜色
            self.window.fill(COLOR_BLACK)
            # 让背景图片循环滚动
            bg1.displayBackGround()
            bg2.displayBackGround()
            bg1.rect.left -= STEP
            bg2.rect.left -= STEP
            # print(bg1.rect.left, bg2.rect.left)
            if bg1.rect.left <= -WIN_WIDTH*2:
                bg1.rect.left = bg2.rect.left + bg2.rect.width
            if bg2.rect.left <= -WIN_WIDTH*2:
                bg2.rect.left = bg1.rect.left + bg1.rect.width
            # 监听事件
            self.getEvent()
            # 展示player
            MainGame.player.display()
            # 检测是否碰撞到障碍物
            MainGame.player.hitObstacle()
            # 遍历障碍物列表，展示每个障碍物并移动
            for obstacle in MainGame.obstacleList:
                obstacle.display()
                obstacle.move()
            # 当障碍物移左边屏幕外，从列表中删除,并创一个新的障碍物加入列表
            for obstacle in MainGame.obstacleList:
                if obstacle.rect.left < -obstacle.image.get_rect().width:
                    MainGame.obstacleList.remove(obstacle)
                    obstacle = Obstacle(MainGame.left[0])
                    MainGame.obstacleList.append(obstacle)
            # 刷新窗口
            clock.tick(30)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # 如果没在跳跃，则打开跳跃开关，如果已在跳跃中，则无需再次跳跃
                    if not MainGame.player.jumping:
                        MainGame.player.jumping = True
                        MainGame.player.gravity = 15


class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__()


class Player(BaseItem):

    def __init__(self):
        self.image = player_image_list[0]
        self.rect = self.image.get_rect()
        self.rect.top = 300
        self.rect.left = 200
        # 重力
        self.gravity = 20
        # 跳跃开关
        self.jumping = False
        self.hit_count = 0

    def display(self):
        if self.jumping:
            MainGame.player_image_num = 0
            self.gravity -= 1
            self.rect.top -= self.gravity
            if self.gravity == 0:
                self.rect.top += self.gravity
        if self.rect.top >= 300:
            self.rect.top = 300
            self.gravity = 20
            self.jumping = False
            if MainGame.player_image_num <= len(player_image_list)-2:
                MainGame.player_image_num += 1
            else:
                MainGame.player_image_num = 0
        MainGame.window.blit(player_image_list[MainGame.player_image_num], (self.rect.left, self.rect.top))

    def hitObstacle(self):
        for obstacle in MainGame.obstacleList:
            if pygame.sprite.collide_rect(self, obstacle):
                print(f'碰到障碍物:{self.hit_count}')
                music1 = Music('D:/pythonProject/pygame/tank/素材/shot.mp3')
                music1.playMusic(0)
                self.hit_count += 1


class Obstacle(BaseItem):
    def __init__(self, i):
        self.image = random.choice(obstacle_image_list)
        self.rect = self.image.get_rect()
        self.rect.left = WIN_WIDTH + i
        self.rect.top = 312

    # 展示障碍物方法
    def display(self):
        MainGame.window.blit(self.image, (self.rect.left, self.rect.top))

    # 障碍物移动方法
    def move(self):
        self.rect.left -= STEP


class BackGround():
    def __init__(self, map_left):
        self.image = pygame.image.load('素材/map1.png')
        self.rect = self.image.get_rect()
        self.rect.left = map_left
        self.rect.top = 0

    # 背景图循环展示
    def displayBackGround(self):
        MainGame.window.blit(self.image, (self.rect.left, self.rect.top))


class Music():
    def __init__(self, fileName):
        self.fileName = fileName
        pygame.mixer.init()
        pygame.mixer.music.load(self.fileName)

    def playMusic(self, loop):
        pygame.mixer.music.play(loops=loop, start=0.0)


MainGame().startGame()
