import pygame
import sys

pygame.init()       # 初始化pygame
size = width, height = 320, 240     # 设置窗口
screen = pygame.display.set_mode(size)   # 显示窗口

# 执行死循环，确保窗口一直显示
while True:
    for event in pygame.event.get():        # 历遍所有事件
        if event.type == pygame.QUIT:       # 如果单机关闭窗口，则退出
            sys.exit()

pygame.quit()   #   退出pygame
