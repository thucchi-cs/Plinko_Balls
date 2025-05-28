from globals import *
import pygame

class Input:
    def __init__(self, min, max, curr, x, y, label, step=1, prefix=""):
        self.min = min
        self.max = max
        self.x = x
        self.y = y
        self.val = curr
        self.label = font.render(label, False, (255,255,255))
        self.step = step
        self.text = curr
        self.prefix = prefix
        self.apply_val = curr

        self.down_btn_rect = pygame.Rect(self.x-45, self.y+3, 39, 39)
        self.up_btn_rect = pygame.Rect(self.x+206, self.y+3, 39, 39)

    def set_range(self, min, max):
        self.min = min
        self.max = max

    def set_value(self, value):
        self.val = value
        if self.val > self.max:
            self.val = self.max
        elif self.val < self.min:
            self.val = self.min

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (self.x,self.y, 200, 45), 4, 10)
        screen.blit(font.render(self.prefix + str(self.val), False, (255,255,255)), (self.x + 15,self.y+10))
        screen.blit(self.label, (self.x,self.y-40))

        pygame.draw.rect(screen, (255,255,255), self.down_btn_rect, border_radius=5)
        pygame.draw.rect(screen, (255,255,255), self.up_btn_rect, border_radius=5)
        pygame.draw.polygon(screen, (0,0,0), [(self.x-12, self.y+11), (self.x-39, self.y+11), (self.x-26, self.y+34)])        
        pygame.draw.polygon(screen, (0,0,0), [(self.x+212, self.y+34), (self.x+239, self.y+34), (self.x+226, self.y+11)])

    def get_value(self):
        return self.apply_val
    
    def check_clicked(self, mouse):
        if self.down_btn_rect.collidepoint(mouse):
            self.set_value(self.val - self.step)
        elif self.up_btn_rect.collidepoint(mouse):
            self.set_value(self.val + self.step)  

    def check_click():
        mouse = pygame.mouse.get_pos()   
        for k,v in inputs.items():
            v.check_clicked(mouse)

    def draw_all(screen):
        for i in inputs.values():
            i.draw(screen)