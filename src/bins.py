import pygame
from globals import *

pygame.font.init()
font = pygame.font.Font(size=25)

class Bin:
    def __init__(self, bin, x, y, color):
        self.value = bin
        self.x = x
        self.y = y
        self.width = get_bin_size()
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
                self.y = get_bin_y()
    
    def create_bins():
        bin_count = get_bin_count()
        for i in range(bin_count):
            x1 = (i*get_bin_size()) + (i*bin_spacing) + get_bin_start()
            bins.append(Bin(0, x1, get_bin_y(), (255,48,47)))

    def delete_bins():
        bins.clear()
            
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