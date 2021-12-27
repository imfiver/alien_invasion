def score_read_file():
    """从文件读取玩家历史最高分，如果文件为空为文件不存在则默认为0"""
    file_name = "log/score.txt"
    score_max = 0
    try:
        with open(file_name) as file_score:
            for line in file_score:
                if line == '\n' or line == "":
                    return 0
                score = int(line.rstrip())
                if score > score_max:
                    score_max = score
                return score_max
    except FileNotFoundError:
        print("历史最高分文件不存在，设置为0")
        return 0


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        # 游戏刚启动时处于(非)活动状态，点击按钮才启动
        self.game_active = False
        # 在任何情况下都不应该重置当前最高得分
        self.high_score = score_read_file()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        # 等级
        self.level = 1
