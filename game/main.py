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
bg_folder = pygame.image.load('img/bg/folderbg.png').convert_alpha()

#unique
playimg = pygame.image.load('img/playgame.png').convert_alpha()
quitimg = pygame.image.load('img/quit_game.png').convert_alpha()
corelock = pygame.image.load('img/lockcore.png').convert_alpha()
trashcan = pygame.image.load('img/thrashbin.png').convert_alpha()

#reusable
arrowleft = pygame.image.load('img/arrowleft.png').convert_alpha()
folderimg = pygame.image.load('img/folder.png').convert_alpha()
imgimg = pygame.image.load('img/imgimg.png').convert_alpha()






#x, y, image, scale







#main menu
playgame = button.Button(352, 172, playimg, 1)
quit_button = button.Button(896, 476, quitimg, 1)

#"hub"?
core = button.Button(352, 172, corelock, 1)
trash = button.Button(5, 5, trashcan, 1)
folderbutton1 = button.Button(74, 5, folderimg, 1)

#thrash
leftarrow = button.Button(5, 5, arrowleft, 0.5)

#folder1
image1 = button.Button(74, 150, imgimg, 1)
image2 = button.Button(143, 150, imgimg, 1)
image3 = button.Button(212, 150, imgimg, 1)
image4 = button.Button(281, 150, imgimg, 1)
image5 = button.Button(350, 150, imgimg, 1)
image6 = button.Button(419, 150, imgimg, 1)
image7 = button.Button(488, 150, imgimg, 1)


run = True
while run:

    screen.fill((202, 195, 222))

    if location == "main":
        #Main menu
        if playgame.draw(screen) == True:
            pygame.time.wait(100)
            print("Starting game...")
            location = "hub"
        if quit_button.draw(screen) == True:
            pygame.time.wait(100)
            print("Logging off...")
            run = False


    if location == "hub":
        #Hub-esque-thing
        if core.draw(screen) == True:
            pygame.time.wait(100)
            if locked:
                print("A key is needed...")
        if trash.draw(screen) == True:
            pygame.time.wait(100)
            location = "thrash"
        if folderbutton1.draw(screen) == True:
            pygame.time.wait(100)
            location = "folder1"


    if location == "thrash":
        game_display.blit(bg_thrash, (0, 0))

        if leftarrow.draw(screen) == True:
            pygame.time.wait(100)
            location = "hub"
        
    if location == "folder1":
        game_display.blit(bg_folder, (10, 10))
        #folder with hints for code for box
        if folderbutton1.draw(screen) == True:
            pygame.time.wait(100)
            location = "hub"
        if image1.draw(screen) == True:
            pygame.time.wait(100)
            imgshow = "1"
        if image2.draw(screen) == True:
            pygame.time.wait(100)
            imgshow = "2"
        if image3.draw(screen) == True:
            pygame.time.wait(100)
            imgshow = "3"
        if image4.draw(screen) == True:
            pygame.time.wait(100)
            imgshow = "4"
        if image5.draw(screen) == True:
            pygame.time.wait(100)
            imgshow = "5"
        if image6.draw(screen) == True:
            pygame.time.wait(100)
            imgshow = "6"
        if image7.draw(screen) == True:
            pygame.time.wait(100)
            imgshow = "7"





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    pygame.display.update() 

pygame.quit()