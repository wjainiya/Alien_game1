#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
import game_function as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import time
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game() -> object:
    pygame.init()
    # 创建屏幕
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), 0, 32)
    # 标题
    pygame.display.set_caption("Alien invasion")

    # 创建飞机
    ship = Ship(ai_settings, screen)
    print("1:",ship.rect)
    # 创建子弹
    bullets =Group()
    # 创建敌人
    aliens = Group()
    # 创建敌人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建button
    play_button = Button(ai_settings, screen, "Play")
    # 创建信息统计的实例
    stats = GameStats(ai_settings)
    # 创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)

    while True:
        # 检查鼠标和键盘事件
        gf.check_event(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb)

        # 游戏状态
        if stats.game_active:
            # 更新飞船位置
            ship.updat()
            # 更新子弹位置
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, sb, stats)
            # 更新敌人
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

        # 绘制屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats,sb)

        # 延时一下
        time.sleep(0.003)


if __name__ == '__main__':
    run_game()
