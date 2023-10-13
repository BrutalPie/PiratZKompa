from pygame import *
from MenuButton import draw_button, button_rect,button_font

def ret_back(y):
    if y == 0:
        back = transform.scale(image.load('image/island.png'),(1366,768))
    elif y == 1:
        back = transform.scale(image.load('image/cave.png'),(1366,768))
    