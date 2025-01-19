import pygame
from config import *
from helper import *
from plateitems import *

def load_fridge(items: dict): 
    buttons = [] 
    for i, (item, details) in enumerate(items.items()): 
        image = pygame.image.load(details["file"]) 
        resized_image = pygame.transform.scale(image, (50, 50)) 
        button = itemButton(item, resized_image, details["position"][0], details["position"][1], details["type"]) 
        buttons.append(button) 
    return buttons

def points_transition(lst: Bar):
    global state, level, coins
    points_text = font.render(f"Points: {coins}", True, 'black')

    vegCount, wholeGrainsCount, proteinCount = 0, 0, 0

    for item in lst.items: 
        if item.foodtype == "veggies":
            vegCount += 1
        elif item.foodtype == "wholeGrains":
            wholeGrainsCount += 1
        elif item.foodtype == "protein":
            proteinCount += 1
    
    vegPerc = vegCount / 4
    wholeGrainsPerc = wholeGrainsCount / 4
    proteinPerc = proteinCount / 4

    percentages = []
    percentages.append(vegPerc)
    percentages.append(wholeGrainsPerc)
    percentages.append(proteinPerc) 

    ideal_perc = [0.5, 0.25, 0.25]

    for i in range(3):
        if percentages[i] == ideal_perc[i]:
            coins += 3
        elif ideal_perc[i] - 0.2 <= percentages[i] <= ideal_perc[i] + 0.2:
            coins += 1

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

    ## MENU STATE ##
    elif state == "MENU":
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
