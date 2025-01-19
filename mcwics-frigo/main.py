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

screen = pygame.display.set_mode((723, 800))
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 50)
back_surface = pygame.image.load('images/img/BACKGROUNDDDD.jpg')
buttons = pygame.image.load('images/img/BUTTON copy.png')
start_button = nextButton('images/img/start_butt.png',0, 0)
avatar = pygame.image.load('images/img/final.png').convert_alpha()
instruction_txt = pygame.image.load('images/img/instructions.png')
WHITE= (0,0,0)

def get_image(sheet,frame,width,height,colour):
    #image = pygame.Surface((width, height)).convert_alpha()
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width),0,width,height))
    image.set_colorkey(colour)
    return image
        
animation_list = []
animation_steps = 2
last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0

for x in range(animation_steps):
    animation_list.append(get_image(avatar,x,140, 355, WHITE))

run = True
state = "MENU"
level = 1
coins = 0
finished = False

while run:
    screen.fill('white')
    timer.tick(fps)

    ## MENU STATE ##
    if state == "MENU":
        screen.blit(back_surface,(0,0)) 
        screen.blit(buttons, (0,0))
        start_button.draw(screen)

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
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list):
                frame = 0

        screen.blit(animation_list[frame], (400,500))

        #screen.blit(text_surface,(230,50))

        pygame.display.update()
        #clock.tick(60)
        #points_text = font.render(f"Coins: {coins}", True, (0, 0, 0))
        #screen.blit(points_text, ((screen.get_width() - 140) // 2, 20))

    ## INSTRUCTIONS STATE ##
    elif state == "INSTRUCTIONS":
        screen.blit(instruction_txt, (0,0))

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
        else:
            state = "LEVEL_1"

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
