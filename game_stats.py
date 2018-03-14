#!/usr/bin/env python
# -*- coding:utf-8 -*-


class GameStats:
    """跟踪统计游戏的信息"""

    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #在任何时候都不重置最高分
        self.high_score = 0
        # 游戏刚开始的时候处于活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.level = 1
        self.score = 0
        self.ships_left = self.ai_settings.ship_limit
