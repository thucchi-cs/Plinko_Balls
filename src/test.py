import pygame
from constants import *
from pins import Pin
from ball import Ball
from buttons import Ball_Button as bButton
from multipliers import Multiplier

pygame.init()
SCREEN = pygame.display.set_mode((width, height))

pin = Pin(390, 300, pin_radius)
ball = Ball()
ball.x = width//2
ball.y = 100
ball.velocity_y = 2
ball.jump_height = 20

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

    ball.draw(SCREEN)
    ball.fall_test(pin)
    
    pin.draw(SCREEN)

    pygame.display.flip()