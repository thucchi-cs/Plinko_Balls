import pygame
from constants import *
from random import randint
import math

class Ball:
    def __init__(self):
        self.x = randint((pin_start[0] - pin_spacing) + 5, (pin_start[0] + pin_spacing) - 5)
        self.y = 50
        self.rad = ball_radius
        self.max_velocity = 9
        self.velocity_y = 10
        self.velocity_x = 0
        self.gravity = 1
        self.last = self.y
        self.bouncing = False
        self.bounce_height = self.y
        self.bouncy = 2

    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN, (255,0,0), (self.x, self.y), self.rad)

    def check_pin_collision(self):
        space_allowed = ball_radius + pin_radius
        for pin in pins:
            dist = (((self.x - pin.x) ** 2) + ((self.y - pin.y) ** 2))**0.5
            if dist <= space_allowed:
                overlap = space_allowed - dist
                return pin,dist,overlap
        return None
    
    def check_box_collision(self):
        for mul in multipliers:
            center = (self.x + self.rad, self.y + self.rad)
            mul_right = mul.x + mul.width
            mul_bottom = mul.y + mul.height
            if (mul.x <= center[0] <= mul_right) and (mul.y <= center[1] <= mul_bottom):
                mul.text.update_count()
                return mul
        return None

    def fall(self):
        collide = self.check_pin_collision()
        if collide:
            pin = collide[0]
            distx = self.x - pin.x
            disty = self.y - pin.y
            angle = math.atan2(disty, distx)
            self.velocity_x = math.cos(angle) * 3
            self.velocity_y = round(math.sin(angle) * 5, 0)
            if abs(self.velocity_x) <= 0.1:
                if self.x < (width//2):
                    self.x -= 2
                else:
                    self.x += 2
                    
            # if self.x < (width/2 - pin_spacing):
            #     self.x += center_bias / 20
            # elif self.x > (width/2 + pin_spacing):
            #     self.x -= center_bias / 20
                    
        self.y += self.velocity_y
        self.x += self.velocity_x
        self.velocity_y += self.gravity if (self.velocity_y < self.max_velocity) else 0

    def delete():
        for ball in balls:
            if ball.y > ball_remove_y:
                box = ball.check_box_collision()
                box.bouncing = True
                balls.remove(ball)