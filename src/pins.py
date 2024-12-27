import pygame
from constants import *

class Pin:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad

    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN, (255,255,255), (self.x, self.y), self.rad)

    def create_pins():
        for row in range(1, pin_rows + 1):
            offset = (0.5 * pin_spacing) if (row % 2 == 0) else 0
            for col in range(-(row // 2) - 1, ((row - 1) // 2) + 2):
                x = col * pin_spacing + offset + pin_start[0]
                y = row * pin_spacing + pin_start[1]
                pins.append(Pin(x,y,pin_radius))

    def draw_pins(SCREEN):
        for pin in pins:
            pin.draw(SCREEN)