import pygame
from config import *
from helper import *
from levels import *
from plateitems import *

pygame.init()

font = pygame.font.Font('freesansbold.ttf', 18)

pygame.display.set_caption("freegaur")

buttons_1 = load_fridge(level1_items)
buttons_2 = load_fridge(level2_items)
bar_1 = Bar(4)

run = True
while run:
    screen.fill('white')
    timer.tick(fps)

    level = 1
    coins = 0

    ## LEVEL 1

    for button in buttons_1:
        button.draw()

    bar_1.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons_1:
                if button.check_click():
                    if button in bar_1:
                        bar_1.remove_item(button)
                    else:
                        bar_1.add_item(button)
            bar_1.check_click()
    
    pygame.display.flip()
pygame.quit()
