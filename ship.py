#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化图像并设置初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载图像
        self.image = pygame.image.load('./images/plane3.png').convert_alpha()
        # 缩放飞机大小
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom + 2

        # 在飞创的属性center 中储存小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moveing_right = False
        self.moveing_left = False


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def updat(self):
        """根据移动标志调整飞船位置"""
        if self.moveing_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moveing_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect
        self.rect.centerx = self.center

    def ship_center(self):
        """让飞创在屏幕居中"""
        self.center = self.screen_rect.centerx