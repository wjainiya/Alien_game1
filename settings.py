#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Settings:

    # 存储外星人入侵的所有设置的类
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 768
        self.screen_height = 860
        self.bg_color = (128, 190, 190)

        # 飞船移动速度
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = (240, 240, 50)

        # 子弹一直发射 ---等待拓展
        self.bullets_shot_flag = False

        # 限制子弹数量
        self.bullets_allowed = 15

        # 敌人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50

        # 游戏速度节奏
        self.speedup_scale = 1.1
        # 敌人分数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamict_settings()

        # fleet_direction = 1 表示右移 ，-1 左移
        self.fleet_direction = -1

    def initialize_dynamict_settings(self):
        """初始化游戏进行变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 10

        # fleet_direction 为1 表示右 ，-1 为左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)