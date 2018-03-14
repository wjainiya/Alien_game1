#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''表示单个敌人的类'''
    def __init__(self,ai_settings,screen):
        '''初始化敌人并设置起始位置'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载敌人的图像，并设置rect
        self.image = pygame.image.load('./images/enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()

        #每个敌人的最初都在屏幕左上角出现
        self.rect.x = 0
        self.rect.y = 0

        #储存敌人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制敌人'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''向左或右移动敌人'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        # 测试位置
        # print(self.ai_settings.alien_speed_factor,self.ai_settings.fleet_direction,self.rect.x, self.rect.y,self.rect.right,self.rect.left)

    def check_edges(self):
        '''如果敌人撞到屏幕边缘，就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
