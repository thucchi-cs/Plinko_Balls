import pygame
from constants import *
from pins import Pin
from ball import Ball
from buttons import Ball_Button as bButton

pygame.init()
SCREEN = pygame.display.set_mode((width, height))

Pin.create_pins()
balls.append(Ball())
ball_button = bButton()

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ball_button.check_click():
                    balls.append(Ball())
            
    
    # if counter % 40 == 0:
    #     balls.append(Ball())

    for ball in balls:
        ball.fall()
        ball.draw(SCREEN)
    Ball.delete()
    
    ball_button.draw(SCREEN)
    Pin.draw_pins(SCREEN)
    pygame.display.flip()