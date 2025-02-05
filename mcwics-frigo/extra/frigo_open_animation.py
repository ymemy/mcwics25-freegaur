import pygame
from sys import exit

def run_animation():
    pygame.init()

    screen = pygame.display.set_mode((723, 800))
    pygame.display.set_caption('Title')
    clock = pygame.time.Clock()
    test_font = pygame.font.Font(None, 50)
    back_surface = pygame.image.load('background2.jpg')
    #ground_surface = pygame.image.load('ground.jpg')
    #text_surface = test_font.render('FRIGO', False, 'Blue')

    avatar = pygame.image.load('3.png').convert_alpha()
    WHITE= (0,0,0)
    over = pygame.display.set_mode((1000,800))

    def get_image(sheet,frame,width,height,colour):
        #image = pygame.Surface((width, height)).convert_alpha()
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width),0,width,height))
        image.set_colorkey(colour)
        return image
    def fade(width, height):
        fade = pygame.Surface((width,height))
        fade.fill((255,255,255))
        for alpha in range(0,255):
            fade.set_alpha(alpha)
            #redrawWindow()
            over.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(5)

    def redrawWindow():
        over.fill((255,255,255))


    animation_list = []
    animation_steps = 3
    last_update = pygame.time.get_ticks()
    animation_cooldown = 500
    frame = 0

    for x in range(animation_steps):
        animation_list.append(get_image(avatar,x,257,690, WHITE))

    animation_playing = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #screen.blit(ground_surface,(0,0))
        screen.blit(back_surface,(0,0)) 
        #screen.blit(text_surface,(230,50))

        #display image
        #update animation
        current_time = pygame.time.get_ticks()
        if animation_playing and current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list):
                animation_playing = False
                #frame = 0
                fade(723,800)
        if animation_playing:
            screen.blit(animation_list[frame], (107,0))
        else:
            screen.fill((255,255,255))

        pygame.display.update()
        clock.tick(60)