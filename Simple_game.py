import pygame
pygame.init()
#mandatry functions rquariedt ot star game

screen_size = pygame.display.set_mode((1920, 1080)) #remeber to ad () to fit 2 numbers
#pygame.display.set_mode() setting screnn size

pygame.display.set_caption("Simple game")
#seting window name

white_color = (255, 255, 255)
black_color = (0, 0, 0)
#seting collors

user_heigt_y = 200
user_width_x = 100
#user sizes

user_position_y = 200
user_position_x = 200
#player position

user_movment = 20

game_status = True
while game_status:

    pygame.time.delay(80)
    #slowing game (framerate idk)

    for user_action in pygame.event.get():
        #going thurgut all action in pygame
        if user_action.type == pygame.QUIT:
            game_status = False
            #if user click "X" run  quting scrip form pygame and brak function

    keyboard_input = pygame.key.get_pressed()
    #singing pyfunction "presing keyboard" to keyboard_inpunt

    if keyboard_input[pygame.K_w]:
        user_position_y -= user_movment

    if keyboard_input[pygame.K_s]:
        user_position_y += user_movment

    if keyboard_input[pygame.K_a]:
        user_position_x -= user_movment

    if keyboard_input[pygame.K_d]:
        user_position_x += user_movment
    #control user movment

    screen_size.fill(black_color)
    #calling function "pygame.display" singnet to screen_size

    pygame.draw.rect(screen_size, white_color, (user_position_x, user_position_y, user_width_x,user_heigt_y))
    #redawing screnn-size, player color, (palyer positionxy + sizexy)

    pygame.display.update()
    #refresh game

pygame.quit()
#when player click "X" clsoe window