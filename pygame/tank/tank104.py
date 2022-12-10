'''
V1.04
新增功能
    加载我方坦克

'''

import pygame


VERSION = 'V1.04'
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_RED = pygame.Color(255, 0, 0)


class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    # 创建我方坦克
    TANK_P1 = None

    def __init__(self):
        pass

    # 开始游戏方法
    def startGame(self):
        # 初始化游戏
        pygame.display.init()
        # 创建窗口，加载窗口
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        MainGame.TANK_P1 = Tank(350, 450)
        # 设置标题
        pygame.display.set_caption('坦克大战' + VERSION)
        # 创建文字画布
        textsurface = self.getTextSurface('剩下的敌方坦克数量为%d辆'%5)
        # 让窗口持续刷新
        while True:
            # 给窗口填充颜色
            self.window.fill(COLOR_BLACK)
            # 获取事件
            self.getEvent()
            # 将文字画布blit到窗口中
            self.window.blit(textsurface, (10, 10))
            # 将坦克到窗口中
            self.TANK_P1.displayTank()
            pygame.display.update()

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
                elif event.key == pygame.K_RIGHT:
                    print("坦克向右调头，移动")
                elif event.key == pygame.K_UP:
                    print("坦克向上调头，移动")
                elif event.key == pygame.K_DOWN:
                    print("坦克向下调头，移动")
                elif event.key == pygame.K_SPACE:
                    print("坦克发射子弹")

    # 绘制文字
    def getTextSurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 获取系统支持的所有字体
        fontlist = pygame.font.get_fonts()
        print(fontlist)
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
        self.images={
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
    # 坦克移动方法
    def move(self):
        pass

    # 坦克射击方法
    def shot(self):
        pass

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
