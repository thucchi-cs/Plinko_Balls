import pygame

width = 800
height = 800
fps = 30

pins = []
pin_rows = 10
pin_start = (width//2, width//30)
pin_spacing = width // (pin_rows + 2)
pin_radius = width // 100

ball_radius = pin_spacing // 5
balls = []
ball_remove_y = height - pin_start[1]
