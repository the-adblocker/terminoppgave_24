import pygame
import button


screen_h = 540
screen_w = 960
location = "main"
locked = True
code_slots = False
slot1 = 0
slot2 = 0
slot3 = 0
slot4 = 0

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('button plural')

game_display = pygame.display.set_mode((screen_w, screen_h))

bg_thrash = pygame.image.load('img/bg/thrashbg.png').convert_alpha()
bg_folder = pygame.image.load('img/bg/folderbg.png').convert_alpha()
bg_pir8 = pygame.image.load('img/bg/pir8bg.png').convert_alpha()


#THE GOD DAMN NUMBERS AAAAAAAAA
img0 = pygame.image.load('img/number/0.png').convert_alpha()
img1 = pygame.image.load('img/number/1.png').convert_alpha()
img2 = pygame.image.load('img/number/2.png').convert_alpha()
img3 = pygame.image.load('img/number/3.png').convert_alpha()
img4 = pygame.image.load('img/number/4.png').convert_alpha()
img5 = pygame.image.load('img/number/5.png').convert_alpha()
img6 = pygame.image.load('img/number/6.png').convert_alpha()
img7 = pygame.image.load('img/number/7.png').convert_alpha()
img8 = pygame.image.load('img/number/8.png').convert_alpha()
img9 = pygame.image.load('img/number/9.png').convert_alpha()

#hint picture files
hint1img = pygame.image.load('img/hints/hint1.png').convert_alpha()
hint2img = pygame.image.load('img/hints/hint2.png').convert_alpha()
hint3img = pygame.image.load('img/hints/hint3.png').convert_alpha()
hint4img = pygame.image.load('img/hints/hint4.png').convert_alpha()
hint5img = pygame.image.load('img/hints/fhint1.png').convert_alpha()
hint6img = pygame.image.load('img/hints/fhint2.png').convert_alpha()
hint7img = pygame.image.load('img/hints/fhint3.png').convert_alpha()

#unique
playimg = pygame.image.load('img/playgame.png').convert_alpha()
quitimg = pygame.image.load('img/quit_game.png').convert_alpha()
corelock = pygame.image.load('img/lockcore.png').convert_alpha()
trashcan = pygame.image.load('img/thrashbin.png').convert_alpha()
pir8img = pygame.image.load('img/pir8cove.png').convert_alpha()
chest = pygame.image.load('img/chest.png').convert_alpha()
numslots = pygame.image.load('img/num_code.png').convert_alpha()

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
pir8cove = button.Button(891, 5, pir8img, 1)

# pir8's cove

#thrash
leftarrow = button.Button(5, 5, arrowleft, 0.5)
codechest = button.Button(450, 270, chest, 1.5)
numcode = button.Button(200, 150, numslots, 1)


#numbers first slot qwq
slot1_0 = button.Button(205, 160, img0, 1)
slot1_1 = button.Button(205, 160, img1, 1)
slot1_2 = button.Button(205, 160, img2, 1)
slot1_3 = button.Button(205, 160, img3, 1)
slot1_4 = button.Button(205, 160, img4, 1)
slot1_5 = button.Button(205, 160, img5, 1)
slot1_6 = button.Button(205, 160, img6, 1)
slot1_7 = button.Button(205, 160, img7, 1)
slot1_8 = button.Button(205, 160, img8, 1)
slot1_9 = button.Button(205, 160, img9, 1)


#numbers second slot qwq
slot2_0 = button.Button(325, 160, img0, 1)
slot2_1 = button.Button(325, 160, img1, 1)
slot2_2 = button.Button(325, 160, img2, 1)
slot2_3 = button.Button(325, 160, img3, 1)
slot2_4 = button.Button(325, 160, img4, 1)
slot2_5 = button.Button(325, 160, img5, 1)
slot2_6 = button.Button(325, 160, img6, 1)
slot2_7 = button.Button(325, 160, img7, 1)
slot2_8 = button.Button(325, 160, img8, 1)
slot2_9 = button.Button(325, 160, img9, 1)

#numbers third slot qwq
slot3_0 = button.Button(450, 160, img0, 1)
slot3_1 = button.Button(450, 160, img1, 1)
slot3_2 = button.Button(450, 160, img2, 1)
slot3_3 = button.Button(450, 160, img3, 1)
slot3_4 = button.Button(450, 160, img4, 1)
slot3_5 = button.Button(450, 160, img5, 1)
slot3_6 = button.Button(450, 160, img6, 1)
slot3_7 = button.Button(450, 160, img7, 1)
slot3_8 = button.Button(450, 160, img8, 1)
slot3_9 = button.Button(450, 160, img9, 1)

#numbers fourth slot qwq
slot4_0 = button.Button(570, 160, img0, 1)
slot4_1 = button.Button(570, 160, img1, 1)
slot4_2 = button.Button(570, 160, img2, 1)
slot4_3 = button.Button(570, 160, img3, 1)
slot4_4 = button.Button(570, 160, img4, 1)
slot4_5 = button.Button(570, 160, img5, 1)
slot4_6 = button.Button(570, 160, img6, 1)
slot4_7 = button.Button(570, 160, img7, 1)
slot4_8 = button.Button(570, 160, img8, 1)
slot4_9 = button.Button(570, 160, img9, 1)

#folder1
image1 = button.Button(74, 150, imgimg, 1)
image2 = button.Button(143, 150, imgimg, 1)
image3 = button.Button(212, 150, imgimg, 1)
image4 = button.Button(281, 150, imgimg, 1)
image5 = button.Button(350, 150, imgimg, 1)
image6 = button.Button(419, 150, imgimg, 1)
image7 = button.Button(488, 150, imgimg, 1)

hint1 = button.Button(582, 163, hint1img, 1)
hint2 = button.Button(580, 159, hint2img, 1)
hint3 = button.Button(579, 157, hint3img, 1)
hint4 = button.Button(582, 161, hint4img, 1)
hint5 = button.Button(580, 160, hint5img, 1)
hint6 = button.Button(579, 158, hint6img, 1)
hint7 = button.Button(582, 162, hint7img, 1)


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
            imgshow = "0"
        if pir8cove.draw(screen) == True:
            pygame.time.wait(100)
            location = "pir8"
            imgshow = "0"



    if location == "pir8":
        game_display.blit(bg_pir8, (0, 0))
        if leftarrow.draw(screen) == True:
            pygame.time.wait(100)
            location = "hub"


    if location == "thrash":
        game_display.blit(bg_thrash, (0, 0))

        if leftarrow.draw(screen) == True:
            pygame.time.wait(100)
            location = "hub"
            code_slots = False
        if codechest.draw(screen) == True:
            pygame.time.wait(150)
            code_slots = True
        if code_slots:
            numcode.draw(screen)

            #thanks andy(andreas) for match cases

            #Change slot 1
            match slot1:
                case 0:
                    if slot1_0.draw(screen) == True:
                        pygame.time.wait(100)
                        slot1 = 1
                case 1:
                    if slot1_1.draw(screen) == True:
                        pygame.time.wait(100)
                        slot1 = 2
                case 2:
                    if slot1_2.draw(screen) == True:
                        pygame.time.wait(100)
                        slot1 = 3
                case 3:
                    if slot1_3.draw(screen) == True:
                        pygame.time.wait(100)
                        slot1 = 4
                case 4:
                    if slot1_4.draw(screen) == True:
                        pygame.time.wait(100)
                        slot1 = 5
                case 5:
                    if slot1_5.draw(screen) == True:
                        pygame.time.wait(100)
                        slot1 = 6
                case 6:
                    if slot1_6.draw(screen) == True:
                        pygame.time.wait(100)
                        slot1 = 7
                case 7:
                    if slot1_7.draw(screen) == True:
                        pygame.time.wait(100)
                        slot1 = 8
                case 8:
                    if slot1_8.draw(screen) == True:
                        pygame.time.wait(100)
                        slot1 = 9
                case 9:
                    if slot1_9.draw(screen) == True:
                        pygame.time.wait(100)
                        slot1 = 0


            #Change slot 2
            match slot2:
                case 0:
                    if slot2_0.draw(screen) == True:
                        pygame.time.wait(100)
                        slot2 = 1
                case 1:
                    if slot2_1.draw(screen) == True:
                        pygame.time.wait(100)
                        slot2 = 2
                case 2:
                    if slot2_2.draw(screen) == True:
                        pygame.time.wait(100)
                        slot2 = 3
                case 3:
                    if slot2_3.draw(screen) == True:
                        pygame.time.wait(100)
                        slot2 = 4
                case 4:
                    if slot2_4.draw(screen) == True:
                        pygame.time.wait(100)
                        slot2 = 5
                case 5:
                    if slot2_5.draw(screen) == True:
                        pygame.time.wait(100)
                        slot2 = 6
                case 6:
                    if slot2_6.draw(screen) == True:
                        pygame.time.wait(100)
                        slot2 = 7
                case 7:
                    if slot2_7.draw(screen) == True:
                        pygame.time.wait(100)
                        slot2 = 8
                case 8:
                    if slot2_8.draw(screen) == True:
                        pygame.time.wait(100)
                        slot2 = 9
                case 9:
                    if slot2_9.draw(screen) == True:
                        pygame.time.wait(100)
                        slot2 = 0


            #Change slot 3
            match slot3:
                case 0:
                    if slot3_0.draw(screen) == True:
                        pygame.time.wait(100)
                        slot3 = 1
                
                case 1:
                    if slot3_1.draw(screen) == True:
                        pygame.time.wait(100)
                        slot3 = 2
                case 2:
                    if slot3_2.draw(screen) == True:
                        pygame.time.wait(100)
                        slot3 = 3
                case 3:
                    if slot3_3.draw(screen) == True:
                        pygame.time.wait(100)
                        slot3 = 4
                case 4:
                    if slot3_4.draw(screen) == True:
                        pygame.time.wait(100)
                    slot3 = 5
                case 5:
                    if slot3_5.draw(screen) == True:
                        pygame.time.wait(100)
                        slot3 = 6
                case 6:
                    if slot3_6.draw(screen) == True:
                        pygame.time.wait(100)
                        slot3 = 7
                case 7:
                    if slot3_7.draw(screen) == True:
                        pygame.time.wait(100)
                        slot3 = 8
                case 8:
                    if slot3_8.draw(screen) == True:
                        pygame.time.wait(100)
                        slot3 = 9
                case 9:
                    if slot3_9.draw(screen) == True:
                        pygame.time.wait(100)
                        slot3 = 0


            #Change slot 4
            match slot4:
                case 0:
                    if slot4_0.draw(screen) == True:
                        pygame.time.wait(100)
                        slot4 = 1
                case 1:
                    if slot4_1.draw(screen) == True:
                        pygame.time.wait(100)
                        slot4 = 2
                case 2:
                    if slot4_2.draw(screen) == True:
                        pygame.time.wait(100)
                        slot4 = 3
                case 3:
                    if slot4_3.draw(screen) == True:
                        pygame.time.wait(100)
                        slot4 = 4
                case 4:
                    if slot4_4.draw(screen) == True:
                        pygame.time.wait(100)
                        slot4 = 5
                case 5:
                    if slot4_5.draw(screen) == True:
                        pygame.time.wait(100)
                        slot4 = 6
                case 6:
                    if slot4_6.draw(screen) == True:
                        pygame.time.wait(100)
                        slot4 = 7
                case 7:
                    if slot4_7.draw(screen) == True:
                        pygame.time.wait(100)
                        slot4 = 8
                case 8:
                    if slot4_8.draw(screen) == True:
                        pygame.time.wait(100)
                        slot4 = 9
                case 9:
                    if slot4_9.draw(screen) == True:
                        pygame.time.wait(100)
                        slot4 = 0

               
            
        
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
        match imgshow:
            case "5":
                if hint1.draw(screen) == True:
                    pygame.time.wait(100)
                    imgshow = "0"
            case "3":
                if hint2.draw(screen) == True:
                    pygame.time.wait(100)
                    imgshow = "0"
            case "6":
                if hint3.draw(screen) == True:
                    pygame.time.wait(100)
                    imgshow = "0"
            case "1":
                if hint4.draw(screen) == True:
                    pygame.time.wait(100)
                    imgshow = "0"
            case "4":
                if hint5.draw(screen) == True:
                    pygame.time.wait(100)
                    imgshow = "0"
            case "2":
                if hint6.draw(screen) == True:
                    pygame.time.wait(100)
                    imgshow = "0"
            case "7":
                if hint7.draw(screen) == True:
                    pygame.time.wait(100)
                    imgshow = "0"





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    pygame.display.update() 

pygame.quit()


