import pygame

win_width = 1600
win_height = 750

width = 800
height = 750
board_start = ((win_width-width)//2)
fps = 30

center_left = board_start + (5*width//12)
center_left2 = board_start + (3*width//12)
center_right = board_start + (2*(width//3))

pins = []
bins = []
balls = []
inputs = {}
buttons = {}

pin_start = (width//2 + board_start, 5)
bin_colors = [ (255,0,63), (255,48,47), (255,96,32), (255,144,16), (255,192,0) ]
bin_values = [18, 4, 1.7, 0.9, 0.5]
center_bias = 0.6

bin_values = [
    {"value": 500, "static": True},
    {"value": 100, "static": True},
    {"value": 8, "static": False},
    {"value": 4, "static": False},
    {"value": 2, "static": False},
    {"value": 1, "static": False},
    {"value": 0.5, "static": False},
    {"value": 0.5, "static": False},
    {"value": 1, "static": False},
    {"value": 2, "static": False},
    {"value": 4, "static": False},
    {"value": 8, "static": False},
    {"value": 100, "static": True},
    {"value": 500, "static": True}
]

def get_rows():
    if not inputs.get("row_num"):
        return 9
    return int(inputs.get("row_num").get_value())

def get_pin_spacing(rows=0):
    rows = get_rows() if not rows else rows
    return width // (rows + 2)

def get_pin_radius(rows=0):
    rows = get_rows() if not rows else rows
    return 13 - (rows//1.8)

def get_bin_count(rows=0):
    rows = get_rows() if not rows else rows
    return rows+1

def get_bin_size(pin_spacing=0, pin_radius=0, rows=0):
    rows = get_rows() if not rows else rows
    pin_spacing = get_pin_spacing(rows) if not pin_spacing else pin_spacing
    pin_radius = get_pin_radius(rows) if not pin_radius else pin_radius
    return pin_spacing - 2*pin_radius

def get_bin_start(pin_spacing=0, rows=0, pin_radius=0):
    rows = get_rows() if not rows else rows
    pin_spacing = get_pin_spacing(rows) if not pin_spacing else pin_spacing
    pin_radius = get_pin_radius(rows) if not pin_radius else pin_radius
    return (win_width - (pin_spacing * (1+rows)) + (2*pin_radius)) // 2

def get_bin_spacing(rows=0, pin_radius=0):
    rows = get_rows() if not rows else rows
    pin_radius = get_pin_radius(rows) if not pin_radius else pin_radius
    return 2*pin_radius
    
def get_bin_y(pin_spacing=0, pin_radius=0, rows=0):
    rows = get_rows() if not rows else rows
    pin_spacing = get_pin_spacing(rows) if not pin_spacing else pin_spacing
    pin_radius = get_pin_radius(rows) if not pin_radius else pin_radius
    return pin_start[1] + rows * pin_spacing + 2 *pin_radius

def get_ball_radius(rows=0):
    rows = get_rows() if not rows else rows
    return 13-(rows//5)

def get_ball_remove_y(pin_spacing=0, pin_radius=0, rows=0):
    return get_bin_y(pin_spacing, pin_radius, rows)
