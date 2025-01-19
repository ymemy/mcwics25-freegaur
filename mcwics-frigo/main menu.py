import pygame
from sys import exit
import frigo_open_animation

pygame.init()

class nextButton():
    def __init__(self, image, x_pos, y_pos):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self):
        button_rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        pygame.draw.rect(screen, 'black', button_rect, 0, 5)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        if left_click and button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False

screen = pygame.display.set_mode((723, 800))
pygame.display.set_caption('game')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
back_surface = pygame.image.load('images/img/BACKGROUNDDDD.jpg')
#ground_surface = pygame.image.load('ground.jpg')
#text_surface = test_font.render('FRIGO', False, 'Blue')
start_button = nextButton('images/img/BUTTON copy.png',0,0)


avatar = pygame.image.load('images/img/final.png').convert_alpha()
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
    start_button.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.check_click():
                #file called frigo_open_animations starts running 
                frigo_open_animation.run_animation()
                


    #screen.blit(ground_surface,(0,0))
    screen.blit(back_surface,(0,0)) 
    screen.blit(start_button, (0,0))

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
    clock.tick(60)