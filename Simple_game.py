import os
import sys
import pygame
pygame.init()

# Fixing missing phoTO
if getattr(sys, 'frozen', False):  # checking IF FILE IS OPENING AS EXE
    base_path = sys._MEIPASS  # idk what im doingE
else:
    base_path = os.path.dirname(__file__)  # Ustalamy bazową ścieżkę dla skryptu Python

#mandatry functions rquariedt ot star game

screen_size = pygame.display.set_mode((1665 , 935)) #remeber to ad () to fit 2 numbers
#pygame.display.set_mode() setting screnn size

pygame.display.set_caption("Simple game")
#seting window name

white_color = (255, 255, 255)
black_color = (0, 0, 0)
#seting collors

player_avatar = pygame.image.load(os.path.join(base_path, "Creative (33a).png")) # plis work as EXE pls
#here we loading our spirite

player_avatar = pygame.transform.scale(player_avatar, (100, 150))
#chaingi avata's size width + height


#user_heigt_y = 50
#user_width_x = 20
#user sizes

user_position_y = 100
user_position_x = 100
#player position

user_movment = 5

game_status = True
while game_status:

    pygame.time.delay(10)
    #slowing game (framerate idk)

    for user_action in pygame.event.get():
        #going thurgut all action in pygame
        if user_action.type == pygame.QUIT:
            game_status = False
            #if user click "X" run  quting scrip form pygame and brak function

    keyboard_input = pygame.key.get_pressed()
    #singing pyfunction "presing keyboard" to keyboard_inpunt

    if keyboard_input[pygame.K_w]:
        if user_position_y <= -15:
            user_position_y = -15
        else:
            user_position_y -= user_movment

    if keyboard_input[pygame.K_s]:
        if user_position_y >= 795:
            user_position_y = 795
        else:
            user_position_y += user_movment

    if keyboard_input[pygame.K_a]:
        if user_position_x <= -27:
            user_position_x = -27           #1665 , 935    100, 150
        else:
            user_position_x -= user_movment

    if keyboard_input[pygame.K_d]:
        if user_position_x >= 1587:
            user_position_x = 1587
        else:
            user_position_x += user_movment
    #control user movment

    screen_size.fill(black_color)
    #calling function "pygame.display" singnet to screen_size

    screen_size.blit(player_avatar, (user_position_x, user_position_y))
    #now we using srite so we dond need sizes and screen cuz it is in  pygame.display.update()
    ##oldredawing screnn-size, player color, (palyer positionxy + sizexy)

    pygame.display.update()
    #refresh game

pygame.quit()
#when player click "X" clsoe window