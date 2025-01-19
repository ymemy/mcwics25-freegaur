import pygame
from config import *

class itemButton():
    def __init__(self, text, image, x_pos, y_pos, foodtype, status=False):
        self.text = text
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.foodtype = foodtype
        self.status = status

    def draw(self): 
        if self.status:
            button_rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
            dimmed_image = self.image.copy()
            dimmed_image.fill((0, 0, 0, 100), special_flags=pygame.BLEND_RGBA_MULT)
            screen.blit(dimmed_image, button_rect)

        else:
            button_rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
            screen.blit(self.image, button_rect)
        
        if self.check_hover(): 
            self.show_identifier()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        if left_click and button_rect.collidepoint(mouse_pos):
            self.status = not self.status
            return True
        return False
        
    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        return button_rect.collidepoint(mouse_pos)
        
    def show_identifier(self):
        identifier_text = pygame.font.Font('freesansbold.ttf', 18).render(self.text, True, 'black')
        text_rect = identifier_text.get_rect()
        text_rect.centerx = screen.get_width() // 2 
        text_rect.top = 10
        screen.blit(identifier_text, text_rect)

class nextButton():
    def __init__(self, image, x_pos, y_pos):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self):
        button_rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        screen.blit(self.image, button_rect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        if left_click and button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False
