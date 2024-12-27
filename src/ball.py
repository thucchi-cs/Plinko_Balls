import pygame
from constants import *
from random import randint

class Ball:
    def __init__(self):
        self.x = randint((pin_start[0] - pin_spacing), (pin_start[0] + pin_spacing))
        self.y = 100
        self.rad = ball_radius
        self.speed = 5

    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN, (255,0,0), (self.x, self.y), self.rad)

    def check_pin_collision(self):
        space_allowed = ball_radius + pin_radius
        for pin in pins:
            dist = (((self.x - pin.x) ** 2) + ((self.y - pin.y) ** 2))**0.5
            if dist <= space_allowed:
                return pin
        return None

    def fall(self):
        self.y += self.speed

    def delete():
        for ball in balls:
            if ball.y > ball_remove_y:
                balls.remove(ball)