from pygame import *
from Display_Set import *
#Головний класс з бібліотеки Pygame для створення/додавання/обробки/тд спрайтів
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):

        sprite.Sprite.__init__(self)
    
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#класс ворога який наслідує класс GameSprite
class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self,x1,x2):
        if self.rect.x <= x1: 
            self.side = "right"
        if self.rect.x >= x2:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed