import pygame

screen = pygame.display.set_mode([723, 800])

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
        bar_shadow = pygame.Rect(140, screen.get_height() - 150, screen.get_width() - 280, 90)
        bar_area = pygame.Rect(150, screen.get_height() - 150, screen.get_width() - 300, 80)
        screen.fill((102, 49, 25), bar_shadow)
        screen.fill((132, 64, 35), bar_area)

        for i, item in enumerate(self.items):
            if self.max_items == 8:
                item_rect = item.image.get_rect(topleft=(bar_area.left + i * 50, screen.get_height() - 135))
            else:
                item_rect = item.image.get_rect(topleft=(bar_area.left + i * 60 + 10, screen.get_height() - 135))
            screen.blit(item.image, item_rect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        bar_area = pygame.Rect(150, screen.get_height() - 150, screen.get_width() - 300, 80)
        for item in self.items:
            if self.max_items == 8:
                item_rect = item.image.get_rect(topleft=(bar_area.left + self.items.index(item) * 50, bar_area.top + 10))
            else:
                item_rect = item.image.get_rect(topleft=(bar_area.left + self.items.index(item) * 60 + 10, bar_area.top + 10))
            if left_click and item_rect.collidepoint(mouse_pos):
                self.remove_item(item)
                return True
        return False

