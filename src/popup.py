import pygame
from globals import *
from buttons import Input_Button as btn
from input import Input

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 40)

class Popup:
    def init(x=0):
        Popup.x = 0.25 * win_width
        Popup.y = 0.1 * win_height
        Popup.w = 0.5 * win_width
        Popup.h = 0.5 * win_height
        Popup.color = (0, 46, 93)
        Popup.blur = pygame.Surface((win_width, win_height), pygame.SRCALPHA)
        Popup.btn = btn((win_width//2) - 140, Popup.y+270, "Startbtn.png", "Startbtn.png", False)
        Popup.show = True
        Popup.title = font.render("Starting Balance", False, (255,255,255))
        Popup.input = Input(100, 1000000, 5000, (win_width//2)-225, Popup.y+120, "", w=450, h=75, font=60, money=True)

    def draw(screen):
        if Popup.show:
            Popup.blur.fill((0,0,0,180))
            screen.blit(Popup.blur, (0,0))
            pygame.draw.rect(screen, Popup.color, (Popup.x, Popup.y, Popup.w, Popup.h), border_radius=15)
            Popup.btn.draw(screen)
            screen.blit(Popup.title, ((win_width//2)-(Popup.title.get_width()//2),Popup.y+50))
            Popup.input.draw(screen)
    
    def update():
        if Popup.show:
            mouse = pygame.mouse.get_pos()
            Popup.input.check_clicked(mouse)
            if Popup.btn.check_click():
                Popup.show = False