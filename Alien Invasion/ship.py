import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, screen, ai_settings):
        """Инициализация корабля и задание начальной позиции"""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_width = ai_settings.screen_width
        self.screen_height = ai_settings.screen_height

        # Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/main_ship.png')
        self.w_h = self.image.get_width() / self.image.get_height()

        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()

        # Корабль появляется у левого края экрана
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left + 10

        # Сохранение вещественной координаты центря корабля
        self.centery = float(self.rect.centery)
        self.centerx = float(self.rect.centerx)

        # Флаги перемещения
        self.moving_down = False
        self.moving_up = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Обновляет позицию коробля с учетом флага"""
        # Обновляется атрибут self.center, не rect
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.y > 0:
            self.centery -= self.ai_settings.ship_speed_factor

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor

        # Обновление атрибута rect, на основании атрибута self.center
        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

    def blit_me(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре левой стороны"""
        self.centery = self.screen_rect.centery
        self.centerx = self.rect.width // 2
