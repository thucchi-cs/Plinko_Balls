import pygame
from globals import *

class Ball_Button:
    def __init__(self):
        self.w = width // 6
        self.h = self.w // 4
        self.x = ((width // 2) + board_start) - self.w // 2
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, (0, 255, 0), (self.x, self.y, self.w, self.h))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
        

class Input_Button:
    def __init__(self, x, y, img, img_disabled):
        self.x = x
        self.y = y
        self.img = pygame.image.load(f"graphics/{img}")
        self.disabled = pygame.image.load(f"graphics/{img_disabled}")
        self.isDisabled = True
        self.rect = pygame.Rect(x,y, self.img.get_width(), self.img.get_height())

    def draw(self, screen):
        screen.blit(self.img if not self.isDisabled else self.disabled, (self.x,self.y))

    def toggle_disabled(self, disabled:bool):
        self.isDisabled = disabled

    def check_click(self):
        if not self.isDisabled:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                return True
            return False
        return False