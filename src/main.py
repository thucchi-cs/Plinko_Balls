import pygame
from constants import *
from pins import Pin
from ball import Ball
from buttons import Ball_Button as bButton
from multipliers import Multiplier

pygame.init()
SCREEN = pygame.display.set_mode((width, height))

Pin.create_pins()
balls.append(Ball())
ball_button = bButton()

Multiplier.create_multipliers()

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
            if event.button == 1:
                if ball_button.check_click():
                    balls.append(Ball())

    Ball.delete()
    for ball in balls:
        ball.fall_test2()
        ball.draw(SCREEN)
        
    for mul in multipliers:
        mul.draw(SCREEN)
        mul.bounce()
    ball_button.draw(SCREEN)
    Pin.draw_pins(SCREEN)
    pygame.display.flip()