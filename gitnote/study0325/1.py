# -*- coding:utf-8 -*-
import pygame
import time
from pygame.locals import *
import random

#
class Plane(object):
    # 初始化
    def __init__(self, screen, x, y, image_path):
        self.x = x
        self.y = y
        self.screen = screen
        #  添加一个我方飞机
        self.plane = pygame.image.load(image_path)
        # 子弹列表
        self.bullet_list = []

    def display(self):
        # 6.将飞机添加到窗口中
        self.screen.blit(self.plane, (self.x, self.y))
        # 装越界的子弹
        bullet_list_remove = []
        # 遍历子弹列表
        for bullet in self.bullet_list:
            # 子弹显示与运动
            bullet.display()
            bullet.move()
            # 判断是否出界
            if bullet.judge():
                bullet_list_remove.append(bullet)
        for i in bullet_list_remove:
            self.bullet_list.remove(i)


# 定义子弹的父类
class Bullet(object):
    def __init__(self, screen, x, y, image_path):
        self.x = x
        self.y = y
        self.screen = screen
        self.bullet = pygame.image.load(image_path)
        self.bullet1 = pygame.image.load(image_path)
        self.bullet2 = pygame.image.load(image_path)

    # 显示子弹
    def display(self):
        self.screen.blit(self.bullet1, (self.x - 10, self.y))
        self.screen.blit(self.bullet2, (self.x + 10, self.y))
        self.screen.blit(self.bullet, (self.x, self.y))


# 定义我方子弹
class HeroBullet(Bullet):
    # 初始化动作
    def __init__(self, screen, x, y):
        image_path = "./feiji/HeroBullet1.png"
        Bullet.__init__(self, screen, x + 9, y - 15, image_path)

    def display(self):
        super().display()

    # 向上移动
    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

    # 判断是否击中敌机
    def judge_jizhong(self, enemy):
        if self.x > enemy.x and self.x < enemy.x + 56:
            if self.y > enemy.y and self.y < enemy.y + 31:
                print("击中了敌机")
                return True
        return False


# 我方飞机
class HeroPlane(Plane):
    # 初始化
    def __init__(self, screen):
        image_path = "./feiji/hero.png"
        super().__init__(screen, (240 - 27) / 2, 400 - 50, image_path)

    # self.enemy=enemy

    def display(self):
        Plane.display(self)
        # self.enemy ?  enemy.bobm ?  bullet.judge_jizhong ?
        for bullet in self.bullet_list:
            if bullet.judge_jizhong(self.enemy):
                self.enemy.bomb(True)

    # 添加左右移动的动作

    def move_left(self):
        if self.x > 5:
            self.x -= 5

    def move_right(self):
        if self.x < 210:
            self.x += 5

    def move_up(self):
        if self.y > 5:
            self.y -= 5

    def move_down(self):
        if self.y < 340:
            self.y += 5

    # 开火的动作
    def fire(self, enemy):
        self.enemy = enemy
        self.bullet_list.append(HeroBullet(self.screen, self.x, self.y))


# 定义敌方子弹
class EnemyBullet(Bullet):
    # 初始化动作
    def __init__(self, screen, x, y):
        image_path = "./feiji/EnemyBullet1.png"
        super().__init__(screen, x + 20, y + 30, image_path)

    def display(self):
        Bullet.display(self)

    # 向下移动
    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 400:
            return True
        else:
            return False


# 敌人飞机类
class EnemyPlane(Plane):
    def __init__(self, screen):
        image_path = "./feiji/enemy3.png"
        Plane.__init__(self, screen, 10, 10, image_path)
        self.direction = "right"  # right向右，left向左

        # 定义爆炸效果内容
        self.bomb_image_list = []
        self.__get_bomb_image()
        self.isbomb = False
        self.num = 1
        self.image_num = 0  # 显示过的图片有几张  数量
        self.image_index = 0  # 要显示的图片  数量

    # 加载爆炸图片
    def __get_bomb_image(self):
        for i in range(1, 7):
            image_path = "./planeboom/Plane_Boom_0" + str(i) + ".png"
            self.bomb_image_list.append(pygame.image.load(image_path))
        # 记录图片列表长度
        self.image_length = len(self.bomb_image_list)

    def bomb(self, flag):
        self.isbomb = flag

    # 外层有whlie Ture
    # 显示敌人飞机
    def display(self):

        if self.isbomb:

            bomb_image = self.bomb_image_list[self.image_index]
            # 将图片显示在窗口上
            self.screen.blit(bomb_image, (self.x, self.y))
            # 改变遍历image_num
            self.image_num += 1  # 让每一张图片多停留一会
            # 判断image_num是否在列表长度范围内
            if self.image_num == (self.image_length + 1):
                self.image_num = 0
                self.image_index += 1

                if self.image_index > (self.image_length - 1):
                    self.image_index = 0
                    self.isbomb = False
                    if self.num <= 3:
                        self.display()
                        self.num += 1
                    else:
                        time.sleep(2)
                        exit()
        else:
            super().display()

    # 敌机发射子弹
    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 10 or random_num == 20:
            self.bullet_list.append(
                EnemyBullet(self.screen, self.x, self.y)
            )

    # 左右移动
    def move(self):
        # 判断是否越界
        if self.x > 175:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

        # 根据方向改运动方向
        if self.isbomb:
            return
        else:
            if self.direction == "right":
                self.x += 3
            elif self.direction == "left":
                self.x -= 3


def control_key(hero, enemy):
    for event in pygame.event.get():
        # 判断是否点击了退出按钮
        if event.type == QUIT:
            # 退出
            print("exit")
            exit()
        # 判断是否按下了键
        if event.type == KEYDOWN:
            # 检查按钮是否是a或者left
            if event.key == K_LEFT or event.key == K_a:
                print("left")
                hero.move_left()
            # 检查按钮是否是d或者right
            elif event.key == K_RIGHT or event.key == K_d:
                # 右方向键
                print("right")
                hero.move_right()
            elif event.key == K_UP or event.key == K_w:
                # 上方向键
                print("up")
                hero.move_up()
            elif event.key == K_DOWN or event.key == K_s:
                # 下方向键
                print("down")
                hero.move_down()
            elif event.key == K_SPACE:
                # 上方向键
                time.sleep(0.02)
                print("space-空格建")
                hero.fire(enemy)
            elif event.key == K_b:
                print("bomb")
                enemy.isbomb = True


def main():
    # 播放背景音乐
    # 初始化背景音乐
    pygame.mixer.init()
    # 设置音量
    pygame.mixer.music.set_volume(100)

    pygame.mixer.music.load("./bgmusic/bgm_zhandou1.mp3")
    # 循环播放多少次
    pygame.mixer.music.play(1)

    pygame.init()
    # 设置键盘重复键
    pygame.key.set_repeat(True)
    # 1. 创建窗口  set_mode(元组，flags,depth)   元组 窗口的大小
    screen = pygame.display.set_mode((240, 400), 0, 32)
    # 2. 创建背景
    background = pygame.image.load("./feiji/background.png")
    # 定义飞机在屏幕中出现的位置

    # 添加一个飞机对象
    hero = HeroPlane(screen)
    enemy = EnemyPlane(screen)
    while True:
        # 3. 将背景添加到窗口
        screen.blit(background, (0, 0))
        # 将飞机对象显示在窗口
        hero.display()
        # 通过键盘控制飞机
        control_key(hero, enemy)
        enemy.display()
        enemy.move()
        enemy.fire()
        # 4. 更新显示内容
        pygame.display.update()

        # 休息一会儿
        time.sleep(0.01)


if __name__ == "__main__":
    main();
