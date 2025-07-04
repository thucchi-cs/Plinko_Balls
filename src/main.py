import asyncio
import pygame
import math
from globals import *
from pins import Pin
from ball import Ball
from bins import Bin
from input import Input
from buttons import Input_Button as iButton
from balance import Balance
from popup import Popup

pygame.init()

async def main():
    restart = True
    while restart:
        Popup.init()
        Balance.init(1220, 80, 5000)

        buttons["rows"] = iButton(335, 85, "Applybtn.png", "ApplybtnDisabled.png")
        inputs["row_num"] = Input(9, 13, 11, 80, 80, "Rows", step=1)
        buttons["balls_num"] = iButton(335, 205, "Applybtn.png", "ApplybtnDisabled.png")
        inputs["balls_num"] = Input(1, 5, 1, 80, 200, "Balls At Once", step=1)
        inputs["bet_amount"] = Input(0, Balance.value, 10, 80, 320, "Bet Amount", step=0.01, money=True)
        buttons["restart"] = iButton(1500, 80, "restart.png", "restart.png", False)

        Bin.create_bins()
        Pin.create_pins()
        # balls.append(Ball())
        buttons["balls"] = iButton(80, 380, "Dropbtn.png", "DropbtnDisabled.png", disabled=False)

        SCREEN = pygame.display.set_mode((win_width, height))
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
                    restart = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        restart = False
                    if event.key == pygame.K_SPACE and not Popup.show:
                        for i in range(inputs["balls_num"].get_value()):
                            balls.append(Ball())
                    # if event.key == pygame.K_SPACE:
                    #     balls[-1].bouncing = True
                    
                    for k,v in inputs.items():
                        v.update(event)

                    Popup.input.update(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    Popup.update()
                    if event.button == 1 and not Popup.show:
                        Input.check_click()
                        if buttons["balls"].check_click():
                            buttons.get("balls").toggle_disabled(True)
                            if Balance.value >= (inputs["bet_amount"].get_value() * inputs["balls_num"].get_value()):
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
                        if buttons["restart"].check_click():
                            run = False

            inputs["bet_amount"].max = Balance.value
            inputs["balls_num"].max = math.floor(Balance.value / (inputs["bet_amount"].get_value() if inputs["bet_amount"].get_value() else 1))

            Ball.delete()
            for ball in balls:
                ball.fall()
                ball.draw(SCREEN)
                
            for bin in bins:
                bin.draw(SCREEN)
                bin.bounce()

            for pin in pins:
                pin.bounce()

            pointer = False
            for btn in buttons.values():
                if btn.check_click():
                    pointer = True
                btn.draw(SCREEN)

            if pointer:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            Balance.draw(SCREEN)

            Pin.draw_pins(SCREEN)

            Input.draw_all(SCREEN)

            Popup.draw(SCREEN)

            pygame.display.flip()

            await asyncio.sleep(0)
        
        Bin.delete_bins()
        Pin.delete_pins()
        balls.clear()

asyncio.run(main())