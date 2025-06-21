import pygame
from globals import *

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 36)

class Balance:
    def init(x, y, starting):
        Balance.x = x
        Balance.y = y
        Balance.value = starting
        Balance.label = font.render("Balance", False, (255,255,255))

    def add(value, multiplier=1):
        Balance.value += value * multiplier
    
    def subtract(value, multiplier=1):
        Balance.value -= value * multiplier

    def draw(screen):
        pygame.draw.rect(screen, (255,255,255), (Balance.x,Balance.y, 240, 50), 4, 10)
        screen.blit(font.render(f"$ {Balance.value:.2f}", False, (255,255,255)), (Balance.x + 15,Balance.y+10))
        screen.blit(Balance.label, (Balance.x,Balance.y-40))