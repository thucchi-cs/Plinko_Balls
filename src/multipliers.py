import pygame
from constants import *

pygame.font.init()
font = pygame.font.Font(size=25)

class Multiplier:
    def __init__(self, multiplier, x, y, color):
        self.value = multiplier
        self.x = x
        self.y = y
        self.width = multi_size
        self.height = self.width // 2
        self.color = color
        self.bouncing = False
        self.bounce_velocity = 2
        self.bounce_height = 4
        self.bounce_resistance = 1
        self.text = self.Counter((self.x + self.width // 2), (self.y + self.height // 2))
        
    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height), border_radius = 5)
        SCREEN.blit(self.text.text, self.text.rect)
        
    def bounce(self):
        if self.bouncing: 
            self.y += self.bounce_velocity
            self.bounce_velocity -= self.bounce_resistance
            if self.bounce_velocity < -self.bounce_height:
                self.bouncing = False
                self.bounce_velocity = 2
                self.y = multi_y
    
    def create_multipliers():
        for i in range(multi_count//2):
            x1 = (i*multi_size) + (i*multi_spacing) + multi_start
            x2 = ((multi_count - 1 - i)*multi_size) + ((multi_count - 1 - i)*multi_spacing) + multi_start
            multipliers.append(Multiplier(0, x1, multi_y, (255,48,47)))
            multipliers.append(Multiplier(0, x2, multi_y, (255,48,47)))
            
    class Counter:
        def __init__(self, x, y):
            self.count = 0
            self.text = font.render(str(self.count), True, (0,0,0))
            self.rect = self.text.get_rect()
            self.center = (x,y)
            self.rect.center = self.center
        
        def update_count(self):
            self.count += 1
            self.text = font.render(str(self.count), True, (0,0,0))
            self.rect = self.text.get_rect()
            self.rect.center = self.center