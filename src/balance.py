import pygame
from globals import *

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 36)

class Balance:
    def __init__(self, x, y, starting):
        self.x = x
        self.y = y
        self.value = starting
        self.label = font.render("Balance", False, (255,255,255))

    def add(self, value, multiplier=1):
        self.value += value * multiplier
    
    def subtract(self, value, multiplier=1):
        self.value -= value * multiplier

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (self.x,self.y, 240, 50), 4, 10)
        screen.blit(font.render(f"$ {self.value:.2f}", False, (255,255,255)), (self.x + 15,self.y+10))
        screen.blit(self.label, (self.x,self.y-40))