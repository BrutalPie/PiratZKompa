from pygame import *
from Main import *


def ret_barriers():
    barriers = sprite.Group()

    w1 = GameSprite('image/stone.jpg', 133 * 1.69,380 * 0.83, 400 * 1.69,50 * 0.83)
    w5 = GameSprite('image/stone.jpg', 133 * 1.69,380 * 0.83, 40 * 1.69,400 * 0.83)
    w3 = GameSprite('image/stone.jpg', 133 * 1.69,120 * 0.83, 400 * 1.69,50 * 0.83)
    w2 = GameSprite('image/stone.jpg', 453 * 1.69,800 * 0.83, 400 * 1.69,50 * 0.83)
    w4 = GameSprite('image/stone.jpg', 843 * 1.69,590 * 0.83, 40 * 1.69,400 * 0.83)
    w6 = GameSprite('image/stone.jpg', 133 * 1.69,-250 * 0.83, 40 * 1.69,400 * 0.83)
    purse = GameSprite('image/purse.png', 1290 * 0.73,690 * 1.69, 80 * 0.73,80 * 1.69)
    murders = GameSprite('image/kill.png', 1240,10, 130,130)
    '''w1 = GameSprite('image/stone.jpg', 283 * x_scale, 240 * y_scale, 400 * x_scale, 40 * y_scale)
    w5 = GameSprite('image/stone.jpg', 283 * x_scale, 240 * y_scale, 40 * x_scale, 300 * y_scale)
    w3 = GameSprite('image/stone.jpg', 283 * x_scale, 110 * y_scale, 400 * x_scale, 40 * y_scale)
    w2 = GameSprite('image/stone.jpg', 683 * x_scale, 488 * y_scale, 400 * x_scale, 40 * y_scale)
    w4 = GameSprite('image/stone.jpg', 1043 * x_scale, 228 * y_scale, 40 * x_scale, 400 * y_scale)
    w6 = GameSprite('image/stone.jpg', 283 * x_scale, -250 * y_scale, 40 * x_scale, 400 * y_scale)
    purse = GameSprite('image/purse.png', 1290 * x_scale, 690 * y_scale, 80 * x_scale, 80 * y_scale)
    murders = GameSprite('image/kill.png', 1240 * x_scale, 10 * y_scale, 130 * x_scale, 130 * y_scale)'''

    barriers.add(w1)
    barriers.add(w2)
    barriers.add(w3)
    barriers.add(w4)
    barriers.add(w5)
    barriers.add(w6)
    barriers.add(purse)
    barriers.add(murders)
    return barriers
def ret_monsters():
    monsters = sprite.Group()
    monster1 = Enemy('image/Pumpkin.png', 328, 285, 50, 80, 5)
    monster2 = Enemy('image/Pumpkin.png', 988, 403, 50, 80, 3)
    monster3 = Enemy('image/Pumpkin.png', 1088, 488, 50, 80, 4)
    monster4 = Enemy('image/Pumpkin.png', 228, 240, 50, 80, 2)

    monsters.add(monster1)
    monsters.add(monster2)
    monsters.add(monster3)
    monsters.add(monster4)

    monster1.update(323,993)
    monster2.update(323,993)
    monster3.update(1088,1311)
    monster4.update(0,228)
    return monsters