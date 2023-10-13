from pygame import *


def ret_back(y):
    if y == 0:
        back = transform.scale(image.load('image/island.png'),(1366,768))
    if y == 1:
        back = transform.scale(image.load('image/cave.png'),(1366,768))
    