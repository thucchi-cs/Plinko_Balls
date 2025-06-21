import pygame
from globals import *

class Input_Button:
    def __init__(self, x, y, img, img_disabled, disabled=True):
        self.x = x
        self.y = y
        self.img = pygame.image.load(f"graphics/{img}")
        self.disabled = pygame.image.load(f"graphics/{img_disabled}")
        self.isDisabled = disabled
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