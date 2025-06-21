import pygame
import math
from globals import *
from pins import Pin
from ball import Ball
from buttons import Ball_Button as bButton
from bins import Bin
from input import Input
from buttons import Input_Button as iButton
from balance import Balance

pygame.init()
SCREEN = pygame.display.set_mode((win_width, height))

balance.append(Balance(1300, 80, 5000))

buttons["rows"] = iButton(335, 85, "Applybtn.png", "ApplybtnDisabled.png")
inputs["row_num"] = Input(9, 13, 13, 80, 80, "Rows", step=1)
buttons["balls_num"] = iButton(335, 205, "Applybtn.png", "ApplybtnDisabled.png")
inputs["balls_num"] = Input(1, 5, 1, 80, 200, "Balls At Once", step=1)
inputs["bet_amount"] = Input(0, balance[0].value, 0, 80, 320, "Bet Amount", step=1, money=True)

Bin.create_bins()
Pin.create_pins()
# balls.append(Ball())
buttons["balls"] = iButton(80, 380, "Dropbtn.png", "DropbtnDisabled.png", disabled=False)

clock = pygame.time.Clock()
counter = 0
run = True
while run:
    SCREEN.fill((15,23,40))
    clock.tick(fps)
    counter += 1

    buttons.get("rows").toggle_disabled(len(balls) > 0)
    buttons.get("balls_num").toggle_disabled(len(balls) > 0)
    buttons.get("balls").toggle_disabled(False)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
            if event.key == pygame.K_SPACE:
                for i in range(inputs["balls_num"].get_value()):
                    balls.append(Ball())
            # if event.key == pygame.K_SPACE:
            #     balls[-1].bouncing = True
            
            for k,v in inputs.items():
                v.update(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Input.check_click()
                if buttons["balls"].check_click():
                    buttons.get("balls").toggle_disabled(True)
                    if balance[0].value >= (inputs["bet_amount"].get_value() * inputs["balls_num"].get_value()):
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

    inputs["bet_amount"].max = balance[0].value
    inputs["balls_num"].max = math.floor(balance[0].value / (inputs["bet_amount"].get_value() if inputs["bet_amount"].get_value() else 1))

    Ball.delete()
    for ball in balls:
        ball.fall()
        ball.draw(SCREEN)
        
    for bin in bins:
        bin.draw(SCREEN)
        bin.bounce()

    for pin in pins:
        pin.bounce()

    for btn in buttons.values():
        btn.draw(SCREEN)

    balance[0].draw(SCREEN)

    Pin.draw_pins(SCREEN)

    Input.draw_all(SCREEN)

    # pygame.draw.line(SCREEN, (255,255,0), (center_left,0), (center_left,win_height))
    # pygame.draw.line(SCREEN, (255,255,0), (center_right,0), (center_right,win_height))

    pygame.display.flip()