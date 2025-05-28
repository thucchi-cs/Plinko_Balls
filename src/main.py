import pygame
from globals import *
from pins import Pin
from ball import Ball
from buttons import Ball_Button as bButton
from bins import Bin
from input import Input

pygame.init()
SCREEN = pygame.display.set_mode((win_width, height))

Bin.create_bins()
inputs["row_num"] = Input(9, 13, 9, 80, 80, "Rows", step=1)

Pin.create_pins()
balls.append(Ball())
ball_button = bButton()

# inputs["bet_amount"] = Input(0, 5, 2, 80, 80, "Rows", step=1)

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
            if event.key == pygame.K_RETURN:
                balls.append(Ball())
            if event.key == pygame.K_SPACE:
                balls[-1].bouncing = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            Input.check_click()
            if event.button == 1:
                if ball_button.check_click():
                    balls.append(Ball())

    Ball.delete()
    for ball in balls:
        ball.fall()
        ball.draw(SCREEN)
        
    for mul in bins:
        mul.draw(SCREEN)
        mul.bounce()

    for pin in pins:
        pin.bounce()

    ball_button.draw(SCREEN)
    Pin.draw_pins(SCREEN)

    Input.draw_all(SCREEN)

    pygame.display.flip()