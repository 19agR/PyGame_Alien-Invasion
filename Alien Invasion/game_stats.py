class GameStats:
    """Отслеживание статистики"""

    def __init__(self, ai_settings):
        """Инициализиует статистику"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Игра запускается в неактивном состоянии
        self.game_active = False

        # Рекорд не должен сбрасываться
        file = open('high_score.txt', 'r')
        self.high_score = int(file.read())

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
