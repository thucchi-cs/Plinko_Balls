import pygame
from globals import *
from random import randint, choice
import math
from balance import Balance

class Ball:
    def __init__(self):
        pin_spacing = get_pin_spacing()
        self.x = randint((pin_start[0] - pin_spacing+5), (pin_start[0] + pin_spacing-5))
        self.y = 20
        self.rad = get_ball_radius()
        self.max_velocity = 10
        self.velocity_y = 10
        self.velocity_x = 0
        self.gravity = 1
        self.x_bias = [0.5, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8]

        self.y_dampening = 0.5
        self.x_dampening = 2.5

        Balance.subtract(inputs["bet_amount"].get_value())

    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN, (255,0,0), (self.x, self.y), self.rad)

    def check_pin_collision(self):
        pin_radius = get_pin_radius()
        space_allowed = get_ball_radius() + pin_radius
        for pin in pins:
            dist = (((self.x - pin.x) ** 2) + ((self.y - pin.y) ** 2))**0.5
            if dist <= space_allowed:
                overlap = space_allowed - dist
                return pin,dist,overlap
        return None
    
    def pin_collide(self, pin):
        pin_radius = get_pin_radius()
        space_allowed = get_ball_radius() + pin_radius
        for p in pin:
            dist = (((self.x - p.x) ** 2) + ((self.y - p.y) ** 2))**0.5
            if dist <= space_allowed:
                overlap = space_allowed - dist
                return p,dist,overlap
        return None
    
    def check_box_collision(self):
        pin_rad = get_pin_radius()
        for bin in bins:
            centerx = self.x + self.rad
            bin_right = bin.x + bin.width
            if (bin.x-pin_rad <= centerx <= bin_right+pin_rad):
                bin.update_balance()
                return bin
        return None

    def fall(self, pin=None):
        collide = self.check_pin_collision() if not pin else self.pin_collide(pin)
        if self.velocity_y < self.max_velocity:
            self.velocity_y += self.gravity
        else:
            self.velocity_y = self.max_velocity

        if collide and self.velocity_y > 0:
            angle = math.atan2(collide[0].y-self.y, collide[0].x-self.x)
            self.velocity_y *= -self.y_dampening*math.sin(angle)
            self.velocity_x = self.x_dampening*math.cos(angle)

            if angle == math.radians(90) or angle == math.radians(270):
                self.velocity_x = 1 if randint(0,1) else -1
            elif (self.x < center_left) and (self.velocity_x > 0.5):
                self.x -= self.velocity_x
                self.velocity_x -= choice(self.x_bias)
                if self.x < center_left2:
                    self.velocity_x -= choice(self.x_bias)
                    self.velocity_y -= 2
            elif (self.x > center_right) and (self.velocity_x < 0.5):
                self.x -= self.velocity_x
                self.velocity_x += choice(self.x_bias)

            collide[0].bouncing = True

        self.velocity_y = round(self.velocity_y)
        self.y += self.velocity_y
        self.x -= self.velocity_x

        if self.y > win_height and pin:
            self.y = 100
            self.x = 400
            self.velocity_x = 0
            self.velocity_y = 10

    def delete():
        b = 0
        while b < len(balls):
            if balls[b].y > get_ball_remove_y():
                box = balls[b].check_box_collision()
                if box:
                    box.bouncing = True
                balls.remove(balls[b])
            else:
                b += 1