import pygame
from globals import *
from random import randint
import math

class Ball:
    def __init__(self):
        pin_spacing = get_pin_spacing()
        self.x = randint((pin_start[0] - pin_spacing) + 5, (pin_start[0] + pin_spacing) - 5)
        self.y = 50
        self.rad = get_ball_radius()
        self.max_velocity = 9
        self.velocity_y = 10
        self.velocity_x = 0
        self.gravity = 1
        self.last = self.y
        self.bouncing = False
        self.bounce_height = self.y
        self.bouncy = 2
        self.jump_height = self.velocity_y

        self.y_dampening = 0.33
        self.x_dampening = 0.4

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
        dist = (((self.x - pin.x) ** 2) + ((self.y - pin.y) ** 2))**0.5
        if dist <= space_allowed:
            overlap = space_allowed - dist
            return pin,dist,overlap
        return None
    
    def check_box_collision(self):
        for mul in bins:
            center = (self.x + self.rad, self.y + self.rad)
            mul_right = mul.x + mul.width
            mul_bottom = mul.y + mul.height
            if (mul.x <= center[0] <= mul_right) and (mul.y <= center[1] <= mul_bottom):
                mul.text.update_count()
                return mul
        return None

    def fall(self, pin=None):
        collide = self.check_pin_collision() if not pin else self.pin_collide(pin)
        if collide and not self.bouncing:
            self.bouncing = True
            self.jump_height = self.velocity_y
            self.jump_height = math.ceil(self.jump_height * self.y_dampening)
            self.velocity_y = self.jump_height
            self.velocity_x = abs(self.velocity_y)
            change_x = self.x - collide[0].x
            change_y = self.y - collide[0].y
            angle = math.atan2(change_y, change_x)
            self.velocity_x *= math.cos(angle)
            self.velocity_x *= self.x_dampening
            if self.x > (width * 0.6 + board_start):
                self.velocity_x -= center_bias
            elif self.x < ((width - width * 0.6) + board_start):
                self.velocity_x += center_bias
            self.velocity_x = math.ceil(abs(self.velocity_x)) * (-1 if self.velocity_x < 0 else 1)
            collide[0].bouncing = True


        if self.bouncing and self.velocity_y >= -self.jump_height:
            gravity = 1
            self.y -= self.velocity_y
            self.velocity_y -= gravity

            self.x += math.ceil(self.velocity_x)

            if self.velocity_y < -self.jump_height:
                self.bouncing = False
                self.velocity_y = self.jump_height 
        else:
            self.y += self.velocity_y
            self.x += self.velocity_x
            self.velocity_y += self.gravity

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