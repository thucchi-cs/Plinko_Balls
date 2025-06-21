import pygame
from globals import *
from pins import Pin
from ball import Ball
from buttons import Ball_Button as bButton
from bins import Bin
import math
from input import Input
from buttons import Input_Button as iButton
from balance import Balance

pygame.init()
SCREEN = pygame.display.set_mode((win_width, height))

balance.append(Balance(1300, 80, 5000))

buttons["rows"] = iButton(335, 85, "Applybtn.png", "ApplybtnDisabled.png")
inputs["row_num"] = Input(9, 13, 13, 80, 80, "Rows", step=1)
buttons["balls_num"] = iButton(335, 205, "Applybtn.png", "ApplybtnDisabled.png")
inputs["balls_num"] = Input(1, 5, 1, 80, 200, "Balls At Once", step=1)
inputs["bet_amount"] = Input(0, balance[0].value, 0, 80, 320, "Bet Amount", step=1, money=True)

buttons["balls"] = iButton(80, 380, "Dropbtn.png", "DropbtnDisabled.png", disabled=False)

pin_radius = get_pin_radius()
pin = Pin(400, 300, pin_radius)
pin2 = Pin(380, 600, pin_radius)
ball = Ball()
ball.x = 400
ball.y = 100
# ball.velocity_y = 2
# ball.jump_height = 20

clock = pygame.time.Clock()
counter = 0
run = True
while run:
    SCREEN.fill((15,23,40))
    clock.tick(fps)
    counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
            if event.key == pygame.K_SPACE:
                input.set_value(input.val+1)
            if event.key == pygame.K_RETURN:
                input.set_value(input.val-1)

    ball.fall_test2([pin,pin2])
    ball.draw(SCREEN)
    
    # pin.bounce()
    pin.draw(SCREEN)
    pin2.draw(SCREEN)

    # pygame.draw.line(SCREEN, (255,255,0), ((width - width * 0.6) + board_start, 0), ((width - width * 0.6) + board_start, 800))
    # pygame.draw.line(SCREEN, (255,255,0), (width * 0.6 + board_start, 0), (width * 0.6 + board_start, 800))

    pygame.display.flip()