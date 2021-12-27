class Settings:
    """存储游戏中《外星人游戏》中所有的类"""

    def __init__(self):
        """临时调整颜色"""
        self.blue = (0, 255, 255)
        self.white = (230, 230, 230)
        """临时调整颜色"""

        """初始化游戏的静态设置"""
        # 屏幕设置
        # 设置宽度
        self.screen_width = 1200
        # 设置高度
        self.screen_height = 800
        # 设置背景色
        self.bg_color = self.white

        # 飞船设置
        self.ship_limit = 3  # 飞船数量限制,多少把后重开

        # 子弹设置
        self.bullet_width = 3  # 3000 测试
        self.bullet_height = 15 # 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5  # 3

        # 外星人设置
        self.fleet_drop_speed = 20  # 1.0
        self.speedup_scale = 1.1
        # 外星人分数提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化游戏的动态设置"""
        self.ship_speed = 4.0  # 1.5
        self.bullet_speed = 5.0
        self.alien_speed = 3.0  # 1.0
        self.fleet_direction = 1  # self.fleet_direction为1表示向右移，-1表示向左移
        # 计分
        self.alien_points = 50


    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale )
        # print(self.alien_points)