import pygame
from globals import *

class Pin:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = (255,255,255)
        self.bouncing = False
        self.bounce_count = 0

    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN, self.color, (self.x, self.y), self.rad)

    def create_pins():
        rows = get_rows()
        pin_spacing = get_pin_spacing(rows)
        pin_radius = get_pin_radius(rows)
        for row in range(1, rows + 1):
            offset = (0.5 * pin_spacing) if (row % 2 == 0) else 0
            for col in range(-(row // 2) - 1, ((row - 1) // 2) + 2):
                x = col * pin_spacing + offset + pin_start[0]
                y = row * pin_spacing + pin_start[1]
                pins.append(Pin(x,y,pin_radius))

    def delete_pins():
        pins.clear()

    def draw_pins(SCREEN):
        for pin in pins:
            pin.draw(SCREEN)

    def bounce(self):
        pin_radius = get_pin_radius()
        if self.bouncing:
            self.bounce_count += 1
            if self.bounce_count % 3 == 0:
                self.bounce_count = 0
                self.rad = pin_radius
                self.bouncing = False
            else:
                self.rad = pin_radius * 1.3