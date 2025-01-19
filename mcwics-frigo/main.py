import pygame
from sys import exit
from config import *
from helper import *
from plateitems import *
from frigohelper import *

buttons_1 = load_fridge(level1_items)
buttons_2 = load_fridge(level2_items)
buttons_3 = load_fridge(level3_items)

bar_1 = Bar(4)
bar_2 = Bar(6)
bar_3 = Bar(8)

run = True
state = "FRIGO_OPEN"
level = 1
coins = 0
finished = False

pygame.init()

font = pygame.font.Font('freesansbold.ttf', 18)

pygame.display.set_caption("Food for Thought")

buttons_1 = load_fridge(level1_items)
buttons_2 = load_fridge(level2_items)
buttons_3 = load_fridge(level3_items)

bar_1 = Bar(4)
bar_2 = Bar(6)
bar_3 = Bar(8)

run = True
state = "FRIGO_OPEN"
level = 1
coins = 0
finished = False

while run:
    screen.fill('white')
    timer.tick(fps)

    ## FRIGO OPEN ##
    if state == "FRIGO_OPEN":
        # Display animation frames
        if animation_playing:
            screen.blit(back_surface, (0, 0))
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame += 1
                last_update = current_time
                if frame >= len(animation_list):
                    animation_playing = False
                    fade(723, 800)
            if animation_playing:
                screen.blit(animation_list[frame], (107, 0))
            else:
                screen.fill((255, 255, 255))
        else:
            state = "MENU"

    ## MENU STATE ##
    elif state == "MENU":
        points_text = font.render(f"Coins: {coins}", True, (0, 0, 0))
        screen.blit(points_text, ((screen.get_width() - 140) // 2, 20))

    ## INSTRUCTIONS STATE ##
    elif state == "INSTRUCTIONS":
        pass

    ## LEVEL 1 ##
    if state == "LEVEL_1":
        for button in buttons_1:
            button.draw()

        bar_1.draw(screen)
        next_button.draw()

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
                if next_button.check_click() and len(bar_1.items) == 4:
                    points_transition(bar_1)
                    state = "TRANSITION"
    
    ## LEVEL 2 ##
    elif state == "LEVEL_2":
        for button in buttons_2:
            button.draw()
        
        bar_2.draw(screen)
        next_button.draw()

    ## LEVEL 3 ##
    elif state == "LEVEL_3":
        pass

    ## TRANSITION STATE ##
    elif state == "TRANSITION": 
        points_text = font.render(f"Coins: {coins}", True, (0, 0, 0))
        screen.blit(points_text, ((screen.get_width() - 140) // 2, 20))
        next_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.check_click():
                    state = f"LEVEL_{level + 1}"
                    level += 1

    ## GAME OVER ##
    elif state == "GAME_OVER":
        pass
    
    pygame.display.flip()
pygame.quit()
