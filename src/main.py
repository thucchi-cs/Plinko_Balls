import pygame
from globals import *
from pins import Pin
from ball import Ball
from buttons import Ball_Button as bButton
from bins import Bin
from input import Input
from buttons import Input_Button as iButton

pygame.init()
SCREEN = pygame.display.set_mode((win_width, height))

buttons["rows"] = iButton(335, 85, "Applybtn.png", "ApplybtnDisabled.png")
inputs["row_num"] = Input(9, 13, 11, 80, 80, "Rows", step=1)
buttons["balls_num"] = iButton(335, 205, "Applybtn.png", "ApplybtnDisabled.png")
inputs["balls_num"] = Input(1, 5, 1, 80, 200, "Balls At Once", step=1)
# inputs["bet_amount"] = Input(0, 5, 2, 80, 80, "Rows", step=1)

Bin.create_bins()
Pin.create_pins()
# balls.append(Ball())
buttons["balls"] = bButton()

clock = pygame.time.Clock()
counter = 0
run = True
while run:
    SCREEN.fill((15,23,40))
    clock.tick(fps)
    counter += 1

    buttons.get("rows").toggle_disabled(len(balls) > 0)
    buttons.get("balls_num").toggle_disabled(len(balls) > 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
            if event.key == pygame.K_RETURN:
                for i in range(inputs["balls_num"].get_value()):
                    balls.append(Ball())
            if event.key == pygame.K_SPACE:
                balls[-1].bouncing = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Input.check_click()
                if buttons["balls"].check_click():
                    for i in range(inputs["balls_num"].get_value()):
                        balls.append(Ball())
                if buttons["rows"].check_click():
                    buttons.get("rows").toggle_disabled(True)
                    inputs["row_num"].apply_val = inputs["row_num"].val
                    Bin.delete_bins()
                    Pin.delete_pins()
                    Bin.create_bins()
                    Pin.create_pins()
                if buttons["balls_num"].check_click():
                    inputs["balls_num"].apply_val = inputs["balls_num"].val
                    buttons.get("balls_num").toggle_disabled(True)

    Ball.delete()
    for ball in balls:
        ball.fall()
        ball.draw(SCREEN)
        
    for mul in bins:
        mul.draw(SCREEN)
        mul.bounce()

    for pin in pins:
        pin.bounce()

    for btn in buttons.values():
        btn.draw(SCREEN)

    Pin.draw_pins(SCREEN)

    Input.draw_all(SCREEN)

    pygame.display.flip()