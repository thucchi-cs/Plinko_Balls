import pygame
from constants import *

class Multiplier:
    def __init__(self, multiplier, x, y, color):
        self.value = multiplier
        self.x = x
        self.y = y
        self.width = multi_size
        self.height = self.width // 2
        self.color = color
        self.bouncing = False
        self.bounce_height = self.y - self.height//3
        self.bounce_velocity = 2
        self.bounce_resistance = 1
        
    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height), border_radius = 5)
        
    def bounce(self):
        if self.bouncing: 
            self.y += self.bounce_velocity
            self.bounce_velocity -= self.bounce_resistance
            if self.bounce_velocity >= -self.bounce_height:
                self.bouncing = False
    
    def create_multipliers():
        for i in range(len(multi_colors)):
            x1 = (i*multi_size) + (i*multi_spacing) + multi_start
            x2 = ((multi_count - 1 - i)*multi_size) + ((multi_count - 1 - i)*multi_spacing) + multi_start
            multipliers.append(Multiplier(multi_values[i], x1, multi_y, multi_colors[i]))
            multipliers.append(Multiplier(multi_values[i], x2, multi_y, multi_colors[i]))