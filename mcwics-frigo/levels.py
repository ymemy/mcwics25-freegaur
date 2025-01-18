'''
current_level = 1
levels = [level_1, level_2]

def switch_level():
    global current_level
    current_level += 1
    if current_level < len(levels):
        load_level(levels[current_level])
    else:
        print("You've completed all levels!")'''

import pygame
from config import *
from helper import *

def load_fridge(items: dict): 
    buttons = [] 
    for i, (item, details) in enumerate(items.items()): 
        image = pygame.image.load(details["file"]) 
        resized_image = pygame.transform.scale(image, (50, 50)) 
        button = itemButton(item, resized_image, details["position"][0], details["position"][1]) 
        buttons.append(button) 
    return buttons
