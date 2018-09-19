# -*- coding:utf-8 -*-
import pygame
import time


def main():
    # 1. 创建窗口  set_mode(元组，flags,depth)   元组 窗口的大小
    screen = pygame.display.set_mode((240, 400), 0, 32)
    # 2. 创建背景
    background = pygame.image.load("./feiji/background.png")
    # 5. 添加一个我方飞机
    plane=pygame.image.load("./feiji/hero.png")

    #定义飞机在屏幕中出现的位置
    x=(240-27)/2
    y=400-50

    while True:
        # 3. 将背景添加到窗口
        screen.blit(background, (0, 0))

        # 6.将飞机添加到窗口中
        screen.blit(background, (x,y))

        # 4. 更新显示内容
        pygame.display.update()
        # 休息一会儿
        time.sleep(0.01)


if __name__ == "__main__":
    main()
