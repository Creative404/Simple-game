import os
import sys
from time import sleep

import pygame
from random import randint

pygame.init()
#mandatry functions rquariedt ot star game

color_white = (255, 255, 255)
color_pink = (255, 20, 147)
color_red = (250, 0, 0)
#colors

# Fixing missing phoTO
if getattr(sys, 'frozen', False):  # checking IF FILE IS OPENING AS EXE
    base_path = sys._MEIPASS  # idk what im doingE
else:
    base_path = os.path.dirname(__file__)  # Ustalamy bazową ścieżkę dla skryptu Python

pygame.font.init()
text_parametrs_points = pygame.font.Font(None, 80)
text_parametrs_lives = pygame.font.Font(None, 50)
text_parametrs_end_game = pygame.font.Font(None, 375)
#adding font to game

pygame.mixer.init()
hit_sound = pygame.mixer.Sound(os.path.join(base_path, "Anvil.mp3"))
#adding sounds




screen_size = pygame.display.set_mode((1600 , 900)) #remeber to ad () to fit 2 numbers
#pygame.display.set_mode() setting screnn size

pygame.display.set_caption("Anvil madness")
#seting window name


player_avatar = pygame.image.load(os.path.join(base_path, "Creative (33a).png")) # plis work as EXE pls
anvil_image = pygame.image.load(os.path.join(base_path, "Anvil.png"))
background = pygame.image.load(os.path.join(base_path, "factory.jpeg"))
#here we loading our spirite

player_avatar = pygame.transform.scale(player_avatar, (220, 300))
anvil_image = pygame.transform.scale(anvil_image, (150,120))
background = pygame.transform.scale(background, (1600 , 900))
#chaingi avata's size width + height


user_position_y = 580
user_position_x = -65
#player position

Lives_position_y = user_position_y

anvil_image_y = -120 # -120     900
anvil_image_x = 500 # 0       1450

bacground_y = 0
bacground_x = 0

user_movment = 5
anvil_movment = 5

lives = 3
points = 0

last_hit = 0
game_time = 0

difficulty = 0

game_status = True
while game_status:
    difficulty += 1

    killable_obj = randint(0,1450)


    if difficulty >= 450:
        anvil_movment +=2
        difficulty = 0


    if anvil_image_y >= 900:
        anvil_image_x = killable_obj
        points += 10
        anvil_image_y = 0




    pygame.time.delay(10)
    #slowing game (framerate idk)

    anvil_image_y += anvil_movment

    #if gametime


    for user_action in pygame.event.get():
        #going thurgut all action in pygame
        if user_action.type == pygame.QUIT:
            game_status = False
            #if user click "X" run  quting scrip form pygame and brak function

    keyboard_input = pygame.key.get_pressed()
    #singing pyfunction "presing keyboard" to keyboard_inpunt

    if keyboard_input[pygame.K_a] or keyboard_input[pygame.K_LEFT]:
        if user_position_x <= -65:
            user_position_x = -65
        else:
            user_position_x -= user_movment

    if keyboard_input[pygame.K_d] or keyboard_input[pygame.K_RIGHT]:
        if user_position_x >= 1430:
            user_position_x = 1430
        else:
            user_position_x += user_movment

    lives_display = text_parametrs_lives.render(("Lives: " + str(lives)), True, color_pink)
    points_display = text_parametrs_points.render(("Points: " + str(points)), True, color_white)
    end_screen =text_parametrs_end_game.render("GAME OVER", True, color_red)



    #lives = text_paramters.render(b ,True, pink)
    #parameters render it

    player_hitbox= pygame.Rect(user_position_x, user_position_y, 170, 285)
    anvil_hitbox = pygame.Rect(anvil_image_x, anvil_image_y,87, 92)
    #creatibg rectange "hitbox" gibing postion and x,y

    game_time = pygame.time.get_ticks()

    if anvil_hitbox.colliderect(player_hitbox):
        #if player touch anvil hitbox
        if game_time - last_hit > 1250:
        # cooldown a odjemowanei zycia
            hit_sound.play()
            lives -= 1
            last_hit = game_time



    screen_size.blit(background, (bacground_x, bacground_y))

    screen_size.blit(player_avatar, (user_position_x, user_position_y))
    #now we using srite so we dond need sizes and screen cuz it is in  pygame.display.update()

    ##oldredawing screnn-size, player color, (palyer positionxy + sizexy)
    screen_size.blit(anvil_image, (anvil_image_x, anvil_image_y))

    screen_size.blit(lives_display, (user_position_x + 62, 865))
    screen_size.blit(points_display, (1240, 35))




    pygame.display.update()
    #refresh game
    if lives == -1:
        screen_size.blit(end_screen, (5, 330))
        pygame.display.update()
        sleep(2)
        game_status = False

pygame.quit()
#when player click "X" clsoe window