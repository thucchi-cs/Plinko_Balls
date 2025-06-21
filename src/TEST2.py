import pygame
from globals import *
import math

pygame.init()
SCREEN = pygame.display.set_mode((win_width, height))

x = 800
y = 100
w = 100
h = 50
vy = 5
vx = 0


x2 = 800
y2 = 600
h2 = 30
t2 = y

clock = pygame.time.Clock()
counter = 0
run = True
while run:
    SCREEN.fill((15,23,40))
    clock.tick(fps)
    counter += 1

    x2 = pygame.mouse.get_pos()[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
            if event.key == pygame.K_SPACE:
                x = 800
                y = 100
                w = 100
                h = 50
                vy = 5
                vx = 0
                t = y

    vy += 1
    if ((((x-x2)**2) + ((y-y2)**2))**0.5 < (h+h2)) and (vy>0):
    # if (((y + h) >= (y2-h2)) and vy > 0) and (((x-h) <= (x2-h) <= (x+h)) or ((x-h) <= (x2+h2) <= (x+h))):
        vy *= -0.5

        angle = math.atan2(y2-y, x2-x)
        vy *= 0.5*math.sin(angle)
        vx = 5*math.cos(angle)
    
    vy = round(vy)

    y += vy
    x -= vx

    if y >= win_height:
        x = 800
        y = 100
        w = 100
        h = 50
        vy = 5
        vx = 0
        t = y

    # print(vy)

    pygame.draw.circle(SCREEN, (0,255,255), (x,y), h)
    # pygame.draw.line(SCREEN, (255,255,255), (0, 600), (win_width,600))
    pygame.draw.circle(SCREEN, (255,255,255), (x2,y2),h2)

    pygame.display.flip()