import pygame
import button


screen_h = 540
screen_w = 960
location = "main"
locked = True

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('button plural')

game_display = pygame.display.set_mode((screen_w, screen_h))

bg_thrash = pygame.image.load('img/bg/thrashbg.png').convert_alpha()

#unique
playimg = pygame.image.load('img/playgame.png').convert_alpha()
quitimg = pygame.image.load('img/quit_game.png').convert_alpha()
corelock = pygame.image.load('img/lockcore.png').convert_alpha()
trashcan = pygame.image.load('img/thrashbin.png').convert_alpha()

#resuable
arrowleft = pygame.image.load('img/arrowleft.png').convert_alpha()






#x, y, image, scale

#reusable
leftarrow = button.Button(5, 5, arrowleft, 0.5)


#main menu
playgame = button.Button(352, 172, playimg, 1)
quit_button = button.Button(896, 476, quitimg, 1)

#"hub"?
core = button.Button(352, 172, corelock, 1)
trash = button.Button(5, 5, trashcan, 1)





run = True
while run:

    screen.fill((202, 195, 222))

    if location == "main":
        #Main menu
        if playgame.draw(screen) == True:
            print("Starting game...")
            location = "hub"
        if quit_button.draw(screen) == True:
            print("Logging off...")
            run = False


    if location == "hub":
        #Hub-esque-thing
        if core.draw(screen) == True:
            if locked:
                print("A key is needed...")
        if trash.draw(screen) == True:
            location = "thrash"

    if location == "thrash":
        game_display.blit(bg_thrash, (0, 0))

        if leftarrow.draw(screen) == True:
            location = "hub"
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update() 

pygame.quit()