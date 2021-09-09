class Settings:
    """Класс для хранения настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует статические настройки игры"""
        # Параметры экрана
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (24, 23, 28)

        # Настройки корабля
        self.ship_limit = 3

        # Параметры пули
        self.bullet_width = 330
        self.bullet_height = 15
        self.bullet_color = (200, 60, 60)
        self.bullet_allowed = 5

        # Настройки пришельцев
        self.fleet_drop_speed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.3

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 15
        self.alien_speed_factor = 2.5

        # fleet_direction = 1 обозначает движение вниз; а -1 - вверх
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки сложноси"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

