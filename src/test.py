import pygame
from globals import *
from pins import Pin
from ball import Ball
from buttons import Ball_Button as bButton
from bins import Bin
import math
from input import Input

pygame.init()
SCREEN = pygame.display.set_mode((win_width, height))

pin_radius = get_pin_radius()
pin = Pin(410, 300, pin_radius)
ball = Ball()
ball.x = 400
ball.y = 100
ball.velocity_y = 2
ball.jump_height = 20

input = Input(0, 5, 2, 300, 300, "hello", step=1, prefix="$ ")

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            input.check_click()

    # ball.fall(pin)
    # ball.draw(SCREEN)
    
    # pin.bounce()
    # pin.draw(SCREEN)

    # pygame.draw.line(SCREEN, (255,255,0), ((width - width * 0.6) + board_start, 0), ((width - width * 0.6) + board_start, 800))
    # pygame.draw.line(SCREEN, (255,255,0), (width * 0.6 + board_start, 0), (width * 0.6 + board_start, 800))
    input.draw(SCREEN)

    pygame.display.flip()