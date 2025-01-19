import pygame
from helper import itemButton
from config import *

def load_fridge(items: dict): 
    buttons = [] 
    for i, (item, details) in enumerate(items.items()): 
        image = pygame.image.load(details["file"]) 
        resized_image = pygame.transform.scale(image, (50, 50)) 
        button = itemButton(item, resized_image, details["position"][0], details["position"][1], details["type"]) 
        buttons.append(button) 
    return buttons

def get_image(sheet, frame, width, height, colour):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image.set_colorkey(colour)
    return image

def fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((255, 255, 255))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        redrawWindow()
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

def redrawWindow():
    screen.fill((255, 255, 255))

animation_list = []
animation_steps = 3
last_update = pygame.time.get_ticks()
animation_cooldown = 500
frame = 0

avatar = pygame.image.load('images/img/3.png').convert_alpha()
back_surface = pygame.image.load('images/img/BACKGROUNDDDD.jpg')

for x in range(animation_steps):
    animation_list.append(get_image(avatar, x, 257, 690, WHITE))

animation_playing = True

