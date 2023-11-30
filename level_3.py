from pygame import *
from Main import *
#створення об'єктів(стін), та додавання їх до списку
def ret_barriers():
    barriers = sprite.Group()
    
    w1 = GameSprite('image/stone.jpg', 505 ,315 , 1100, 41)
    w2 = GameSprite('image/stone.jpg', 505 ,664, 1100, 41)
    w3 = GameSprite('image/stone.jpg', 224 ,100 , 676, 41)
    w4 = GameSprite('image/stone.jpg', 224 ,-207 , 67, 332)
    purse = GameSprite('image/purse.png', 1800 ,10 , 120 ,120)
    murders = GameSprite('image/kill.png', 1650,10, 130,130)

    barriers.add(w1)
    barriers.add(w2)
    barriers.add(w3)
    barriers.add(w4)
    barriers.add(purse)
    barriers.add(murders)
    return barriers
#створення об'єктів(монстрів), та додавання їх до списку
def ret_monsters():
    monsters = sprite.Group()
    monster1 = Enemy('image/Pumpkin.png', 300, 165, 50, 80, 5)
    monster2 = Enemy('image/Pumpkin.png', 1500, 230, 50, 80, 3)
    monster3 = Enemy('image/Pumpkin.png', 1340, 578, 50, 80, 4)
    monster4 = Enemy('image/Pumpkin.png', 650, 220, 50, 80, 2)
    monster5 = Enemy('image/Pumpkin.png', 600, 578, 50, 80, 2)

    monsters.add(monster1)
    monsters.add(monster2)
    monsters.add(monster3)
    monsters.add(monster4)
    monsters.add(monster5)

    monster1.update(323,993)
    monster2.update(323,993)
    monster3.update(1088,1311)
    monster4.update(0,228)
    return monsters
#створення об'єктів(монет), та додавання їх до списку
def ret_coin():
    coins = sprite.Group()
    coin1 = GameSprite('image/coin.png', 364,50, 50,50)
    coin2 = GameSprite('image/coin.png', 750,260, 50,50)
    coin3 = GameSprite('image/coin.png', 550,50, 50,50)
    coin4 = GameSprite('image/coin.png', 650,50, 50,50)
    coin5 = GameSprite('image/coin.png', 1150,610, 50,50)
    coin6 = GameSprite('image/coin.png', 1000,610, 50,50)
    coin7 = GameSprite('image/coin.png', 850,610, 50,50)
    coin8 = GameSprite('image/coin.png', 700,610, 50,50)
    coin9 = GameSprite('image/coin.png', 1500,610, 50,50)
    coin10 = GameSprite('image/coin.png', 900,260, 50,50)
    coin11 = GameSprite('image/coin.png', 1050,260, 50,50)
    coin12 = GameSprite('image/coin.png', 1200,260, 50,50)
    coin13 = GameSprite('image/coin.png', 1350,260, 50,50)

    coins.add(coin1)
    coins.add(coin2)
    coins.add(coin3)
    coins.add(coin4)
    coins.add(coin5)
    coins.add(coin6)
    coins.add(coin7)
    coins.add(coin8)
    coins.add(coin9)
    coins.add(coin10)
    coins.add(coin11)
    coins.add(coin12)
    coins.add(coin13)
    return coins
#створення об'єктів(магазин), та додавання їх до списку
def ret_shop():
    shops = sprite.Group()
    shope = GameSprite('image/shop.png', 450,55, 50,50)
    shops.add(shope)
    return shops 