import pygame
from config import *

class Bar(list):
    def __init__(self, max_items):
        self.items = []
        self.max_items = max_items

    def add_item(self, item):
        if len(self.items) < self.max_items and item not in self.items:
            self.items.append(item)
            item.status = True

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            item.status = False

    def draw(self, screen):
        bar_area = pygame.Rect(0, screen.get_height() - 60, screen.get_width(), 60)
        screen.fill((255, 255, 255), bar_area)

        for i, item in enumerate(self.items):
            item_rect = item.image.get_rect(topleft=(i * 60, screen.get_height() - 60))
            screen.blit(item.image, item_rect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        for item in self.items:
            item_rect = item.image.get_rect(topleft=(self.items.index(item) * 60, screen.get_height() - 60))
            if left_click and item_rect.collidepoint(mouse_pos):
                self.remove_item(item)
                return True
        return False

