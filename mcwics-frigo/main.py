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
state = "LEVEL_1"
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

buttons_1 = load_fridge(level1_items)
buttons_2 = load_fridge(level2_items)
buttons_3 = load_fridge(level3_items)

bar_1 = Bar(4)
bar_2 = Bar(6)
bar_3 = Bar(8)

screen = pygame.display.set_mode((723, 800))
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 50)
back_surface = pygame.image.load('images/img/BACKGROUNDDDD.jpg')
inst_back_surface = pygame.image.load('images/img/background2.jpg')
buttons = pygame.image.load('images/img/BUTTON copy.png')
start_button = nextButton('images/img/start_butt.png',0, 0)
next_button2 = nextButton('images/img/NB.png',570, 300)

avatar = pygame.image.load('images/img/final.png').convert_alpha()
instruction_txt = pygame.image.load('images/img/inst.png')
WHITE= (0,0,0)

def get_image(sheet,frame,width,height,colour):
    #image = pygame.Surface((width, height)).convert_alpha()
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width),0,width,height))
    image.set_colorkey(colour)
    return image

#doll animation
animation_list_doll = []
animation_steps_doll = 2
last_update_doll = pygame.time.get_ticks()
animation_cooldown_doll = 200
frame_doll = 0

for x in range(animation_steps_doll):
    animation_list_doll.append(get_image(avatar,x,140, 355, WHITE))


run = True
state = "MENU"
level = 1
coins = 0
finished = False
instruction_txt = pygame.image.load('images/img/inst.png')

def points_transition(lst: Bar):
    global state, level, coins, percentages
    coins, percentages = points_transitions(screen, lst, font, coins)

while run:
    screen.fill('white')
    timer.tick(fps)

    ## MENU STATE ##
    if state == "MENU":
        screen.blit(back_surface,(0,0)) 
        screen.blit(buttons, (0,0))
        start_button.draw(screen)

        current_time = pygame.time.get_ticks()
        if current_time - last_update_doll >= animation_cooldown_doll:
            frame_doll += 1
            last_update_doll = current_time
            if frame_doll >= len(animation_list_doll):
                frame_doll = 0

        screen.blit(animation_list_doll[frame_doll], (400,500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check_click():
                    #file called frigo_open_animations starts running 
                    state = "INSTRUCTIONS"
        #screen.blit(ground_surface,(0,0))

        #display image
        #update animation

        #screen.blit(text_surface,(230,50))

        pygame.display.update()
        #clock.tick(60)
        #points_text = font.render(f"Coins: {coins}", True, (0, 0, 0))
        #screen.blit(points_text, ((screen.get_width() - 140) // 2, 20))

    ## INSTRUCTIONS STATE ##
    elif state == "INSTRUCTIONS":
        screen.blit(inst_back_surface, (0,0))
        screen.blit(instruction_txt, (0,0))
        next_button2.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if next_button2.check_click():
                     state = "FRIGO_OPEN"

    ## FRIGO OPEN ##
    elif state == "FRIGO_OPEN":
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
            pygame.display.update()
            clock.tick(60)
        else:
            state = "LEVEL_1"

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
