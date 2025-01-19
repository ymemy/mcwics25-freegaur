import pygame
from config import *
from helper import *
from plateitems import *

def load_fridge(items: dict): 
    buttons = [] 
    for i, (item, details) in enumerate(items.items()): 
        image = pygame.image.load(details["file"]) 
        resized_image = pygame.transform.scale(image, (50, 50)) 
        button = itemButton(item, resized_image, details["position"][0], details["position"][1]) 
        buttons.append(button) 
    return buttons

def points_transition(lst):
    global state, level, coins
    points_text = font.render(f"Points: {coins}", True, 'black')

    # calculate how many points the player got

    # calculate the percentage of each category
    # check how close to ideal percentage

pygame.init()

font = pygame.font.Font('freesansbold.ttf', 18)

pygame.display.set_caption("freegaur")

buttons_1 = load_fridge(level1_items)
buttons_2 = load_fridge(level2_items)
buttons_3 = load_fridge(level3_items)

bar_1 = Bar(4)
bar_2 = Bar(6)
bar_3 = Bar(8)

run = True
state = "LEVEL_1"
level = 1
coins = 0
finished = False
next_button = nextButton("images/menu_buttons/next.png", (screen.get_width() - 140) // 2 , 700)

while run:
    screen.fill('white')
    timer.tick(fps)

    # show score

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
                    state = "TRANSITION"
    
    elif state == "LEVEL_2":
        for button in buttons_2:
            button.draw()
        
        bar_2.draw(screen)
        next_button.draw()

    elif state == "MENU":
        pass

    elif state == "TRANSITION":
        text_surface = font.render("Score", True, (0, 0, 0))
        screen.blit(text_surface, (WIDTH//2, HEIGHT//2))

    elif state == "GAME_OVER":
        pass

    
    pygame.display.flip()
pygame.quit()
