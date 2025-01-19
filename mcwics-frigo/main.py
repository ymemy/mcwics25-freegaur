import pygame
from sys import exit
from config import *
from helper import *
from plateitems import *
from frigohelper import *

buttons_1 = load_fridge(level1_items)
buttons_2 = load_fridge(level2_items)
buttons_3 = load_fridge(level3_items)

general_bg = pygame.image.load('images/img/background2.jpg')
level_bg = pygame.image.load('images/img/open_fridge.png')

bar_1 = Bar(4)
bar_2 = Bar(6)
bar_3 = Bar(8)

run = True
state = "LEVEL_3"
level = 1
coins = 0
finished = False
percentages = []

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('music/music.mp3') 
pygame.mixer.music.play(-1)

pop_sound = pygame.mixer.Sound('music/pop.mp3')  

font = pygame.font.Font('freesansbold.ttf', 18)
pygame.display.set_caption("Food for Thought")
instruction_txt = pygame.image.load('images/img/instructions.png')

def points_transition(lst: Bar):
    global state, level, coins, percentages
    coins, percentages = points_transitions(screen, lst, font, coins)

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
        screen.blit(instruction_txt, (0,0))
        pass

    ## LEVEL 1 ##
    if state == "LEVEL_1":
        screen.blit(general_bg, (0, 0))
        screen.blit(level_bg, (0, 0))
        for button in buttons_1:
            button.draw()

        bar_1.draw(screen)
        next_button.draw(screen)

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
                    pop_sound.play()
                    points_transition(bar_1)
                    state = "TRANSITION"
    
    ## LEVEL 2 ##
    elif state == "LEVEL_2":
        screen.blit(general_bg, (0, 0))
        screen.blit(level_bg, (0, 0))
        for button in buttons_2:
            button.draw()
        
        bar_2.draw(screen)
        next_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons_2:
                    if button.check_click():
                        if button in bar_2:
                            bar_2.remove_item(button)
                        else:
                            bar_2.add_item(button)
                bar_2.check_click()
                if next_button.check_click() and len(bar_2.items) == 6:
                    pop_sound.play()
                    points_transition(bar_2)
                    state = "TRANSITION"

    ## LEVEL 3 ##
    elif state == "LEVEL_3":
        screen.blit(general_bg, (0, 0))
        screen.blit(level_bg, (0, 0))
        for button in buttons_3:
            button.draw()
        
        bar_3.draw(screen)
        next_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons_3:
                    if button.check_click():
                        if button in bar_3:
                            bar_3.remove_item(button)
                        else:
                            bar_3.add_item(button)
                bar_3.check_click()
                if next_button.check_click() and len(bar_3.items) == 8:
                    pop_sound.play()
                    points_transition(bar_3)
                    state = "TRANSITION"

    ## TRANSITION STATE ##
    elif state == "TRANSITION": 
        screen.blit(general_bg, (0, 0))
        
        points_text = pygame.font.Font('freesansbold.ttf', 60).render(f"Coins: {coins}", True, (73, 45, 32))        
        text_rect = points_text.get_rect(center=(screen.get_width() // 2 + 150, screen.get_height() // 2))
        screen.blit(points_text, text_rect)

        next_button.draw(screen)

        veg_text = font.render(f"Veggies: {percentages[0] * 100:.2f}%", True, (0, 0, 0))
        grains_text = font.render(f"Whole Grains: {percentages[1] * 100:.2f}%", True, (0, 0, 0))
        protein_text = font.render(f"Protein: {percentages[2] * 100:.2f}%", True, (0, 0, 0))

        veg_rect = veg_text.get_rect(center=(screen.get_width() // 2 + 100, screen.get_height() // 2 + 90))
        grains_rect = grains_text.get_rect(center=(screen.get_width() // 2 + 110, screen.get_height() // 2 + 130))
        protein_rect = protein_text.get_rect(center=(screen.get_width() // 2 + 100, screen.get_height() // 2 + 170))

        screen.blit(veg_text, veg_rect)
        screen.blit(grains_text, grains_rect)
        screen.blit(protein_text, protein_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.check_click():
                    pop_sound.play()
                    if level == 3:
                        print("Game over")
                        state = "GAME_OVER"
                    else:
                        state = f"LEVEL_{level + 1}"
                        level += 1

    ## GAME OVER ##
    elif state == "GAME_OVER":
        screen.blit(general_bg, (0, 0))

        points_text = pygame.font.Font('freesansbold.ttf', 50).render(f"Game over!", True, (73, 45, 32))        
        text_rect = points_text.get_rect(center=(screen.get_width() // 2 + 160, screen.get_height() // 2))
        screen.blit(points_text, text_rect)

        next_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.check_click():
                    pop_sound.play()
                    state = "MENU"
    
    pygame.display.flip()
pygame.quit()
