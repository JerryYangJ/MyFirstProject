'''
V1.27
新增功能
    1.优化P2坦克颜色
    2.增加Clock控制帧率
'''
import pygame
import random
import time

VERSION = 'V1.26'
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_RED = pygame.Color(255, 0, 0)

Image_P1 = {
    'U': pygame.image.load('素材/myTank-u.png'),
    'D': pygame.image.load('素材/myTank-d.png'),
    'L': pygame.image.load('素材/myTank-l.png'),
    'R': pygame.image.load('素材/myTank-r.png'),
}
Image_P2 = {
    'U': pygame.image.load('素材/myTankP2-u.png'),
    'D': pygame.image.load('素材/myTankP2-d.png'),
    'L': pygame.image.load('素材/myTankP2-l.png'),
    'R': pygame.image.load('素材/myTankP2-r.png'),
}
Image_Enemy = {
    'U': pygame.image.load('素材/YMM.png'),
    'D': pygame.image.load('素材/YZX.png'),
    'L': pygame.image.load('素材/YZH.png'),
    'R': pygame.image.load('素材/YZH.png'),
}

clock = pygame.time.Clock()


class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    # 创建我方坦克
    TANK_P1 = None
    TANK_P2 = None
    # 敌方坦克列表
    EnemyTank_list = []
    # 要创建的敌方坦克的数量
    EnemyTank_count = 5
    # 存储我方子弹的列表
    Bullet_list = []
    # 存储敌方子弹的列表
    Enemy_Bullet_list = []
    # 存储爆炸效果的列表
    Explode_list = []
    # 墙壁列表
    Wall_list = []
    # 钢铁列表
    Steels_list = []

    def __init__(self):
        pass

    # 开始游戏方法
    def startGame(self):
        # 初始化游戏
        pygame.display.init()
        # 创建窗口，加载窗口
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 设置标题
        pygame.display.set_caption('坦克大战' + VERSION)
        # 创建我方坦克
        self.creatMyTank()
        self.creatMyTankP2()
        # 创建敌方坦克
        self.creatEnemyTank()
        # 创建墙壁
        self.creatWall()
        # 让窗口持续刷新
        while True:
            # 给窗口填充颜色
            self.window.fill(COLOR_BLACK)
            # 获取事件
            self.getEvent()
            # 将文字画布blit到窗口中
            self.window.blit(self.getTextSurface(f'剩下的敌方坦克数量为{len(MainGame.EnemyTank_list)}辆'), (10, 10))
            # 调用墙壁的blit方法，把墙壁blit到窗口中
            self.blitWall()
            # 调用钢铁父类（墙壁）的blit方法，把墙壁blit到窗口中
            self.blitSteels()
            # 将玩家坦克加载到窗口中
            if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                self.TANK_P1.displayTank()
            else:
                del MainGame.TANK_P1
                MainGame.TANK_P1 = None
            if MainGame.TANK_P2 and MainGame.TANK_P2.live:
                self.TANK_P2.displayTank()
            else:
                del MainGame.TANK_P2
                MainGame.TANK_P2 = None
            # 将敌方坦克加载到窗口中
            self.blitEnemyTank()
            # # 调用坦克的移动方法
            # MainGame.TANK_P1.move()
            # 根据坦克的开关状态调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
                # 调用碰撞墙壁的方法
                MainGame.TANK_P1.hitWalls()
                # 我方坦克是否碰撞到敌方坦克
                MainGame.TANK_P1.hitEnemyTank()
            if MainGame.TANK_P2 and not MainGame.TANK_P2.stop:
                MainGame.TANK_P2.move()
                # 调用碰撞墙壁的方法
                MainGame.TANK_P2.hitWalls()
                # 我方坦克是否碰撞到敌方坦克
                MainGame.TANK_P2.hitEnemyTank()
            # 调用渲染子弹列表的方法
            self.blitBullet()
            # 调用敌方渲染子弹列表的方法
            self.blitEnemyBullet()
            # 调用展示爆炸效果的方法
            self.displayExplode()

            # 持续刷新
            clock.tick(30)
            pygame.display.update()

    def creatMyTank(self):
        # 创建我方坦克
        MainGame.TANK_P1 = MyTank(Image_P1, 350, 450)
        # 创建我方坦克出场音效
        # 创建音效对象
        music = Music('素材/start.wav')
        # 调用音效播放方法
        music.play()

    def creatMyTankP2(self):
        # 创建我方坦克
        MainGame.TANK_P2 = MyTank(Image_P2, 300, 450)
        # 创建我方坦克出场音效
        # 创建音效对象
        music = Music('素材/start.wav')
        # 调用音效播放方法
        music.play()

    @classmethod
    def __creatMyTank(cls):
        # 创建我方坦克
        MainGame.TANK_P1 = MyTank(Image_P1, 350, 450)
        # 创建我方坦克出场音效
        # 创建音效对象
        music = Music('素材/start.wav')
        # 调用音效播放方法
        music.play()

    # 创建敌方坦克方法
    def creatEnemyTank(self):
        top = 30
        for i in range(MainGame.EnemyTank_count):
            speed = random.randint(1, 2)
            left = random.randint(1, 7)
            eTank = EnemyTank(Image_Enemy, left * 100, top, speed)
            MainGame.EnemyTank_list.append(eTank)

    # 创建墙壁方法
    def creatWall(self):
        for i in range(1, 30):
            wall = Wall(random.randint(0, 7) * 100, random.randint(1, 5) * 100)
            MainGame.Wall_list.append(wall)
        for n in range(1, 20):
            steel = Steel(random.randint(0, 7) * 100, random.randint(1, 5) * 100)
            MainGame.Steels_list.append(steel)

    # 将墙壁加入到窗口的方法
    def blitWall(self):
        for wall in MainGame.Wall_list:
            if wall.live:
                wall.displayWall()
            else:
                MainGame.Wall_list.remove(wall)

    # 将钢铁加入倒窗口的方法
    def blitSteels(self):
        for steel in MainGame.Steels_list:
            steel.displayWall()

    # 将敌方坦克加入到窗口方法
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if eTank.live:
                eTank.displayTank()
                # 敌方坦克移动
                eTank.randMove()
                # 调用敌方坦克与墙壁的碰撞方法
                eTank.hitMyTank()
                eTank.hitWalls()
                # 调用敌方坦克的射击
                eBullet = eTank.shot()
                # 敌人坦克的shot方法重写后，有可能返回一个None，需要先做判断，当不为None时将子弹存储于敌方子弹列表
                if eBullet:
                    MainGame.Enemy_Bullet_list.append(eBullet)
            else:
                MainGame.EnemyTank_list.remove(eTank)

    # 将我方子弹加入到窗口方法
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            # 如果子弹还活着，则绘制子弹，否则从列表中删除子弹
            if bullet.live:
                bullet.displayBullet()
                # 让子弹移动
                bullet.move()
                # 调用我方坦克子弹与敌方坦克的碰撞方法
                bullet.hitEnemyTank()
                # 调用我方子弹是否碰撞墙壁的方法
                bullet.hitWall()
            else:
                MainGame.Bullet_list.remove(bullet)

    # 将敌方子弹加入到窗口方法
    def blitEnemyBullet(self):
        for eBullet in MainGame.Enemy_Bullet_list:
            # 如果敌方子弹还活着，则绘制子弹，否则从列表中删除子弹
            if eBullet.live:
                eBullet.displayBullet()
                # 让子弹移动
                eBullet.move()
                # 调用子弹是否碰撞墙壁的方法
                eBullet.hitWall()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    eBullet.hitMyTank()
            else:
                MainGame.Enemy_Bullet_list.remove(eBullet)

    # 新增方法：展示所有爆炸效果列表
    def displayExplode(self):
        for explode in MainGame.Explode_list:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.Explode_list.remove(explode)

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
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
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
                            # m = Bullet(MainGame.TANK_P1)
                            m = MainGame.TANK_P1.shot()
                            # 将子弹加入到子弹列表
                            MainGame.Bullet_list.append(m)
                            # 创建发射音效
                            music = Music('素材/shot.mp3')
                            # 播放射击音效
                            music.play()
                        else:
                            print('子弹数量不足')
                            print(f'当前子弹数量为：{len(MainGame.Bullet_list)}')
                if MainGame.TANK_P2 and MainGame.TANK_P2.live:
                    if event.key == pygame.K_a:
                        print("坦克向左调头，移动")
                        # 修改坦克的方向
                        MainGame.TANK_P2.direction = 'L'
                        MainGame.TANK_P2.stop = False
                    elif event.key == pygame.K_d:
                        print("坦克向右调头，移动")
                        MainGame.TANK_P2.direction = 'R'
                        MainGame.TANK_P2.stop = False
                    elif event.key == pygame.K_w:
                        print("坦克向上调头，移动")
                        MainGame.TANK_P2.direction = 'U'
                        MainGame.TANK_P2.stop = False
                    elif event.key == pygame.K_s:
                        print("坦克向下调头，移动")
                        MainGame.TANK_P2.direction = 'D'
                        MainGame.TANK_P2.stop = False
                    elif event.key == pygame.K_j:
                        print("坦克发射子弹")
                        if len(MainGame.Bullet_list) < 3:
                            # 产生一个子弹
                            # m = Bullet(MainGame.TANK_P2)
                            m = MainGame.TANK_P2.shot()
                            # 将子弹加入到子弹列表
                            MainGame.Bullet_list.append(m)
                            # 创建发射音效
                            music = Music('素材/shot.mp3')
                            # 播放射击音效
                            music.play()
                        else:
                            print('子弹数量不足')
                            print(f'当前子弹数量为：{len(MainGame.Bullet_list)}')
                if event.key == pygame.K_ESCAPE and not MainGame.TANK_P1:
                    # 以下三种方式均可，注意区别：类方法不用带参数；实例方法需要带参数；使用实例调用实例方法不用带参数
                    # MainGame.__creatMyTank()   ####??????为什么用MainGame调用时需要增加参数self？
                    # MainGame.creatMyTank(self)
                    self.creatMyTank()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                        # 修改坦克的移动开关
                        MainGame.TANK_P1.stop = True
                if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                    if MainGame.TANK_P2 and MainGame.TANK_P2.live:
                        # 修改坦克的移动开关
                        MainGame.TANK_P2.stop = True

    # 绘制文字
    def getTextSurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 获取系统支持的所有字体
        # fontlist = pygame.font.get_fonts()
        # print(fontlist)
        # 选中一个合适的字体
        font = pygame.font.SysFont('方正舒体', 18)
        textSurface = font.render(text, True, COLOR_RED)
        return textSurface

    # 结束游戏方法
    def endGame(self):
        print('游戏结束')
        exit()


class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__()


class Tank(BaseItem):
    def __init__(self, images, left, top):
        self.images = images
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
        # 增加live属性，用来记录坦克存活状态
        self.live = True
        # 新增属性：用来记录坦克的移动之前的坐标（用于坐标还原时使用）
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    # 坦克移动方法
    def move(self):
        # 记录移动前位置
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
        if self.direction == 'L' and self.rect.left >= 0:
            self.rect.left -= self.speed
        elif self.direction == 'R' and self.rect.left <= MainGame.SCREEN_WIDTH - self.rect.width:
            self.rect.left += self.speed
        elif self.direction == 'U' and self.rect.top >= 0:
            self.rect.top -= self.speed
        elif self.direction == 'D' and self.rect.top <= MainGame.SCREEN_HEIGHT - self.rect.height:
            self.rect.top += self.speed

    # 还原坦克的位置方法
    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop

    # 坦克的碰撞墙壁方法
    def hitWalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall, self):
                self.stay()
        for steel in MainGame.Steels_list:
            if pygame.sprite.collide_rect(steel, self):
                self.stay()

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
    def __init__(self, images, left, top):
        super(MyTank, self).__init__(images, left, top)

    # 新增主动碰撞到敌方坦克的方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank, self):
                self.stay()


class EnemyTank(Tank):
    def __init__(self, images, left, top, speed):
        # 调用父类初始化方法,否则无法调用父类中的live属性（或者在子类中增加一个live属性）
        super(EnemyTank, self).__init__(images, left, top)
        self.images = images
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

    def shot(self):
        num = random.randint(1, 100)
        if num == 1:
            return Bullet(self)

    def displayEnemytTank(self):
        super().displayTank()

    def hitMyTank(self):
        if MainGame.TANK_P1 and pygame.sprite.collide_rect(self, MainGame.TANK_P1):
            self.stay()


class Bullet(BaseItem):
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

    # 我方子弹碰撞敌方坦克的方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank, self):
                # 产生一个爆炸效果
                explode = Explode(eTank)
                # 将爆炸效果加入到爆炸效果列表中
                MainGame.Explode_list.append(explode)
                self.live = False
                eTank.live = False

    # 敌方子弹碰撞我方坦克的方法
    def hitMyTank(self):
        if pygame.sprite.collide_rect(self, MainGame.TANK_P1):
            # 产生爆炸效果，并加入到爆炸效果列表中
            explode = Explode(MainGame.TANK_P1)
            MainGame.Explode_list.append(explode)
            # 修改子弹状态
            self.live = False
            # 修改我方坦克状态
            MainGame.TANK_P1.live = False

    # 子弹与墙壁碰撞的方法
    def hitWall(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall, self):
                # 修改子弹的live属性
                self.live = False
                wall.hp -= 1
                if wall.hp <= 0:
                    wall.live = False
        for steel in MainGame.Steels_list:
            if pygame.sprite.collide_rect(steel, self):
                # 修改子弹的live属性
                self.live = False


class Explode():
    def __init__(self, tank):
        self.rect = tank.rect
        self.step = 0
        self.images = [
            pygame.image.load('素材/爆炸效果1.png'),
            pygame.image.load('素材/爆炸效果2.png'),
            pygame.image.load('素材/爆炸效果3.png'),
            pygame.image.load('素材/爆炸效果4.png'),
        ]
        self.image = self.images[self.step]
        self.live = True

    # 爆炸显示方法
    def displayExplode(self):
        if self.step < len(self.images):
            MainGame.window.blit(self.image, self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0


class Wall():
    def __init__(self, left, top):
        self.image = pygame.image.load('素材/wall.png')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        # 用来判断墙壁是否应该在窗口中展示
        self.live = True
        # 用来记录墙壁的生命值
        self.hp = 3

    # 展示墙壁的方法
    def displayWall(self):
        MainGame.window.blit(self.image, self.rect)


class Steel(Wall):
    def __init__(self, left, top):
        self.image = pygame.image.load('素材/steels.png')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top


class Music():
    def __init__(self, fileName):
        self.fileName = fileName
        # 初始化mixer
        pygame.mixer.init()
        # 加载音效文件
        pygame.mixer.music.load(self.fileName)

    # 音乐播放方法
    def play(self):
        pygame.mixer.music.play(loops=0, start=0.0)  # loop = -1 循环播放


MainGame().startGame()
