import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """Класс для вывода игровой информации"""

    def __init__(self, ai_settings, screen, stats):
        """Инициализует атрибуты подсчета очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Настройки шрифта для вывода счета
        self.text_color = (130, 130, 130)
        self.font = pygame.font.SysFont('', 48)

        # Подготовка изображений счетов
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение"""
        rounded_score = round(self.stats.score, -1)
        score_str = 'Score: {:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Вывод счета в правой левой части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = 'High score: {:,}'.format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # Рекорд выравнивается по центру верхней стороны
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Преобразует уровень в графическое изображение"""
        self.level_image = self.font.render(f"Level: {self.stats.level}", True, self.text_color)

        # Уровень выводится под текущим счетом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.score_rect.left
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Показывает количество оставшихся кораблей"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, self.ai_settings)
            ship.image = pygame.transform.scale(ship.image, (int(ship.rect.width * 0.7),
                                                             int(ship.rect.height * 0.7)))
            ship.image.set_alpha(220)
            ship.rect = ship.image.get_rect()
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = self.ai_settings.screen_height - 10 - ship.rect.height
            self.ships.add(ship)

    def show_score(self):
        """Выводит текущий счет, рекорд и число оставшихся кораблей"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Вывод кораблей
        self.ships.draw(self.screen)
