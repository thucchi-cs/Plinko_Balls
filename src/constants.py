import pygame

width = 800
height = 800
fps = 30

pins = []
pin_rows = 9
pin_start = (width//2, width//30)
pin_spacing = width // (pin_rows + 2)
pin_radius = width // 100

center_bias = 5
multi_count = pin_rows + 1
multi_spacing = width // 100 
# multi_size = (pin_spacing * (pin_rows + 1) - (multi_count-1) * multi_spacing) // multi_count
multi_size = pin_spacing - pin_radius
multi_start = (width - (pin_spacing * (1+pin_rows))) // 2
multi_y = pin_start[1] + pin_rows * pin_spacing + 2 *pin_radius
multi_colors = [ (255,0,63), (255,48,47), (255,96,32), (255,144,16), (255,192,0) ]
multi_values = [18, 4, 1.7, 0.9, 0.5]
multipliers = []

ball_radius = pin_spacing // 5
balls = []
ball_remove_y = multi_y + ball_radius