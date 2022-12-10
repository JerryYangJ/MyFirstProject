import random

import pygame

# 常量
SCALE = 1.6  # 屏幕缩放比例
SCREEN_WIDTH = 512 / SCALE  # 屏幕宽度
SCREEN_HEIGHT = 768 / SCALE  # 屏幕高度
BLACK = (0, 0, 0)  # 颜色-黑色
# 自定义敌机出现时间
CREATE_ENEMY = pygame.USEREVENT

Plane_sprite_group = pygame.sprite.Group()
Bullet_sprite_group = pygame.sprite.Group()
Enemy_sprite_group = pygame.sprite.Group()


class MainGame():
    # 类变量
    screen = None
    bg = None
    # myPlane = None
    bgm = None
    xiaobaozha = None

    def __init__(self):
        pass

    def startGame(self):
        # 游戏循环开关
        run = True
        # 初始化pygame模块
        pygame.init()

        # 创建时钟对象
        clock = pygame.time.Clock()
        pygame.time.set_timer(CREATE_ENEMY, 1000)

        # 创建窗口
        MainGame.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Plane")

        # 创建游戏背景
        MainGame.bg = BackGround(0)
        MainGame.bg1 = BackGround(-SCREEN_HEIGHT)

        # 创建背景音乐并播放
        # MainGame.bgm = Music('素材/audio/bgm_kaichangdonghua.ogg')
        MainGame.bgm = Music('素材/audio/bgm_zhuxuanlv.ogg')
        MainGame.xiaobaozha = Music('素材/audio/effcet_sfx_xiaobaozha.ogg')
        MainGame.bgm.play(0, -1)

        # 创建玩家飞机
        myPlane = Plane()
        Plane_sprite_group.add(myPlane)

        # 游戏循环
        while run:
            # 设置帧率
            clock.tick(30)
            # 获取事件
            self.getEvent()
            # 填充窗口
            MainGame.screen.fill(BLACK)
            # 展示游戏背景
            MainGame.bg.update(MainGame.screen)
            MainGame.bg1.update(MainGame.screen)

            # 碰撞检测
            # print(pygame.sprite.groupcollide(Bullet_sprite_group, Enemy_sprite_group, True, True))

            if len(pygame.sprite.groupcollide(Bullet_sprite_group, Enemy_sprite_group, True, True))>0:
                MainGame.xiaobaozha.play(1, 0)

            # 游戏更新
            Plane_sprite_group.update()
            Enemy_sprite_group.update()
            Bullet_sprite_group.update()

            # 屏幕更新
            Plane_sprite_group.draw(MainGame.screen)
            Enemy_sprite_group.draw(MainGame.screen)
            Bullet_sprite_group.draw(MainGame.screen)
            pygame.display.update()

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.endGame()
            if event.type == CREATE_ENEMY:
                # 创建敌人
                Enemy_sprite_group.add(Enemy(random.randint(50, SCREEN_WIDTH), 0, random.randint(1, 3)))

    def endGame(self):
        exit()


# 游戏背景
class BackGround():
    def __init__(self, y):
        self.initial_y = y
        self.image = pygame.image.load('素材/img_bg_level_1.jpg')
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # 旋转图片
        # self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = y
        self.speed = 3

    def update(self, screen):
        self.rect.y += self.speed
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.y >= SCREEN_HEIGHT:
            self.rect.y = -SCREEN_HEIGHT


class Plane(pygame.sprite.Sprite):
    # 类变量
    fire_rate_num = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 载入飞机图片
        self.image = pygame.image.load('素材/img_plane_main.png')
        # 按窗口大小缩放图片
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_rect().width / SCALE, self.image.get_rect().height / SCALE))
        self.rect = pygame.Rect(0, 0, 135 / SCALE, 91 / SCALE)
        self.image = self.image.subsurface(self.rect)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH / 2 - self.rect.width / 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.speed = 5

    def update(self):
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_list[pygame.K_s] and self.rect.y < SCREEN_HEIGHT - self.rect.height:
            self.rect.y += self.speed
        if key_list[pygame.K_d] and self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += self.speed
        if key_list[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if key_list[pygame.K_SPACE]:
            # 控制涉及冷却时间
            if Plane.fire_rate_num % 5 == 0:
                bullet = self.fire()
                Bullet_sprite_group.add(bullet)
            if Plane.fire_rate_num >= 11:
                Plane.fire_rate_num = 0
            Plane.fire_rate_num += 1
        # screen.blit(self.image, (self.rect.x, self.rect.y))

    def fire(self):
        return Bullet(self)


class Enemy(pygame.sprite.Sprite):
    # 初始化敌人
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        # 载入飞机图片
        self.image = pygame.image.load('素材/img_plane_enemy.png')
        # 按窗口大小缩放图片
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_rect().width / SCALE, self.image.get_rect().height / SCALE))
        self.rect = pygame.Rect(0, 480 / SCALE, 100 / SCALE, 76 / SCALE)
        self.image = self.image.subsurface(self.rect)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width
        self.rect.y = y-self.rect.height
        self.speed = speed

    def update(self):
        if self.rect.y <= SCREEN_HEIGHT:
            self.rect.y += self.speed
            # screen.blit(self.image, (self.rect.x, self.rect.y))
        else:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        # 载入子弹图片
        self.image = pygame.image.load('素材/img_bullet.png')
        # 缩放图片
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_rect().width / (2*SCALE), self.image.get_rect().height /(2*SCALE)))
        self.rect = pygame.Rect(967 / (2*SCALE), 0, 50 / (2*SCALE), 114 / (2*SCALE))
        self.image = self.image.subsurface(self.rect)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width / 2 - self.rect.width / 2
        self.rect.y = player.rect.y - self.rect.height / 2
        self.speed = 10

    def update(self):
        if self.rect.y > -self.rect.height:
            self.rect.y -= self.speed
            # screen.blit(self.image, (self.x, self.y))
        else:
            self.kill()


class Music():
    def __init__(self, filePath):
        # self.fileName = fileName
        pygame.mixer.init()
        # pygame.mixer.music.load(fileName)
        self.sound = pygame.mixer.Sound(filePath)

    def play(self, channel_num, loop):
        # pygame.mixer.music.play(loops=-1)
        pygame.mixer.Channel(channel_num).play(self.sound, loops=loop)


if __name__ == '__main__':
    MainGame().startGame()
