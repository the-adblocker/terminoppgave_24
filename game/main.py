import pygame
import button


screen_h = 540
screen_w = 960

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('button plural')



playimg = pygame.image.load('img/playgame.png').convert_alpha()
quitimg = pygame.image.load('img/quit_game.png').convert_alpha()


#x, y, image, scale
#main menu
playgame = button.Button(352, 172, playimg, 1)
quit_button = button.Button(896, 476, quitimg, 1)


#

run = True
while run:

    screen.fill((202, 195, 222))

    #PUT FUNCTIONALITY HERE
    if playgame.draw(screen) == True:
        print("print a")
    if quit_button.draw(screen) == True:
        print("Logging off...")
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update() 

pygame.quit()