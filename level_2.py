from pygame import *
from Main import *

def ret_barriers():
    barriers = sprite.Group()
    
    w1 = GameSprite('image/stone.jpg', 100 ,300 , 400, 50)
    w5 = GameSprite('image/stone.jpg', 100 ,315 , 67, 332)
    w3 = GameSprite('image/stone.jpg', 224 ,100, 676, 41)
    w2 = GameSprite('image/stone.jpg', 405 ,894, 676, 41)
    w4 = GameSprite('image/stone.jpg', 1124 ,490 , 67, 332)
    w6 = GameSprite('image/stone.jpg', 294 ,-207 , 67, 332)
    purse = GameSprite('image/purse.png', 1800 ,690 , 80 ,80)
    murders = GameSprite('image/kill.png', 1240,10, 130,130)

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