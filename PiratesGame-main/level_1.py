import pygame
from code import GameSprite
def Level_1():
    barriers = GameSprite.sprite.Group()

    w1 = GameSprite('PiratesGame-main/image/stone.jpg', 283,240, 400,40)
    w5 = GameSprite('PiratesGame-main/image/stone.jpg', 283,240, 40,300)
    w3 = GameSprite('PiratesGame-main/image/stone.jpg', 283,110, 400,40)
    w2 = GameSprite('PiratesGame-main/image/stone.jpg', 683,488, 400,40)
    w4 = GameSprite('PiratesGame-main/image/stone.jpg', 1043,228, 40,400)
    w6 = GameSprite('PiratesGame-main/image/stone.jpg', 283,-250, 40,400)
    purse = GameSprite('PiratesGame-main/image/purse.png', 1290,690, 80,80)
    murders = GameSprite('PiratesGame-main/image/kill.png', 1240,10, 130,130)

    barriers.add(w1)
    barriers.add(w2)
    barriers.add(w3)
    barriers.add(w4)
    barriers.add(w5)
    barriers.add(w6)
    barriers.add(purse)
    barriers.add(murders)
    return barriers