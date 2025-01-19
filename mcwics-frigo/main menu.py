import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((723, 800))
pygame.display.set_caption('Title')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
back_surface = pygame.image.load('background2.jpg')
#ground_surface = pygame.image.load('ground.jpg')
text_surface = test_font.render('FRIGO', False, 'Blue')

avatar = pygame.image.load('final.png').convert_alpha()
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
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #screen.blit(ground_surface,(0,0))
    screen.blit(back_surface,(0,0)) 

    #display image
    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    screen.blit(animation_list[frame], (400,450))

    screen.blit(text_surface,(230,50))

    pygame.display.update()
    clock.tick(60)