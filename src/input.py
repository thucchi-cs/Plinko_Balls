from globals import *
import pygame

pygame.font.init()

class Input:
    def __init__(self, min, max, curr, x, y, label, w=200, h=45, font=28, step=1, money=False):
        self.font = pygame.font.Font("freesansbold.ttf", font)
        self.min = min
        self.max = max
        self.x = x
        self.y = y
        self.val = curr
        self.label = self.font.render(label, False, (255,255,255))
        self.step = step
        self.text = curr
        self.money = money
        self.disp_val = curr
        self.apply_val = curr
        self.rect = pygame.Rect(self.x,self.y, w, h)
        self.color = (170,170,170)
        

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
        self.disp_val = self.val

    def draw(self, screen):
        disp = str(self.val) if not self.money or (self.money and (self.apply_val != self.val)) else f"$ {self.apply_val:.2f}"
        pygame.draw.rect(screen, self.color, self.rect, 4, 10)
        screen.blit(self.font.render(disp, False, (255,255,255)), (self.x + 15,self.y+10))
        screen.blit(self.label, (self.x,self.y-40))

        if not self.money:
            btnup_color = (255,255,255) if self.disp_val < self.max else (150,150,150)
            btndown_color = (255,255,255) if self.disp_val > self.min else (150,150,150)
            pygame.draw.rect(screen, btndown_color, self.down_btn_rect, border_radius=5)
            pygame.draw.rect(screen, btnup_color, self.up_btn_rect, border_radius=5)
            pygame.draw.polygon(screen, (0,0,0), [(self.x-12, self.y+11), (self.x-39, self.y+11), (self.x-26, self.y+34)])        
            pygame.draw.polygon(screen, (0,0,0), [(self.x+212, self.y+34), (self.x+239, self.y+34), (self.x+226, self.y+11)])

    def get_value(self):
        return self.apply_val
    
    def check_clicked(self, mouse):
        if not self.money:
            if self.down_btn_rect.collidepoint(mouse):
                self.set_value(self.val - self.step)
            elif self.up_btn_rect.collidepoint(mouse):
                self.set_value(self.val + self.step)  
        if self.rect.collidepoint(mouse):
            self.color = (255,255,255)
            return True
        self.color = (170,170,170)
        self.val = self.disp_val if not self.money else self.apply_val
        return False

    def check_click():
        mouse = pygame.mouse.get_pos()   
        for k,v in inputs.items():
            v.check_clicked(mouse)

    def draw_all(screen):
        for i in inputs.values():
            i.draw(screen)

    def update(self, event):
        if self.color[0] == 255:
            if event.key == pygame.K_RETURN:
                self.color = (170,170,170)
                try:
                    if self.money:
                        self.apply_val = round(float(self.val),2)
                        self.apply_val = self.max if self.apply_val > self.max else self.apply_val
                        self.apply_val = self.min if self.apply_val < self.min else self.apply_val
                        self.val = self.apply_val
                    else:
                        self.disp_val = int(self.val)
                        self.disp_val = self.max if self.disp_val > self.max else self.disp_val
                        self.disp_val = self.min if self.disp_val < self.min else self.disp_val
                        self.val = self.disp_val
                except ValueError:
                    self.val = self.disp_val if not self.money else self.apply_val
                return
            if type(self.val) != str:
                self.val = ""
            if event.key == pygame.K_BACKSPACE:
                self.val = self.val[:-1]
            else:
                self.val += event.unicode