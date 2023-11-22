import pygame
from Main import *
from MenuButton import *
import level_1
pygame.init()

direction = "right"

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):  
        if packman.rect.x <= win_width-60 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0: 
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) 
        if packman.rect.y <= win_height-85 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
                    
    def fire(self,direction):
        bullet = Bullet('image/bullet.png', self.rect.centerx, self.rect.top+40, 15, 15, 15)
        if direction == "left":
            bullets_left.add(bullet)
        elif direction == "right":
            bullets_right.add(bullet)

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self,direction):
        if direction == "left":
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.kill()
        elif direction == "right":
            self.rect.x += self.speed
            if self.rect.x > win_width:
                self.kill()

show_levels = 0
in_level = False
background = None
barriers = None
monsters = None
coins = None
shops =None

def choose_level():
    global background, barriers, monsters, coins, shops, show_levels, in_level
    clicked_button_level = check_button_click_level(mouse_pos)
    if clicked_button_level == "1": 
        print(3)
        import level_1
        background = transform.scale(image.load('image/cave.png'), (win_width, win_height))
        barriers = level_1.ret_barriers()
        monsters = level_1.ret_monsters()
        coins = level_1.ret_coin()
        shops = level_1.ret_shop()
        show_levels = 2
        in_level = True
        
    if clicked_button_level == "2": 
        import level_2
        background = transform.scale(image.load('image/cave.png'), (win_width, win_height))
        barriers = level_2.ret_barriers()
        monsters = level_2.ret_monsters()
        coins = level_2.ret_coin()
        shops = level_2.ret_shop()
        show_levels = 2
        in_level = True
    
    return background, barriers, monsters, coins, shops, show_levels, in_level
    
display.set_caption("Labirint")
back = transform.scale(image.load('image/island.png'),(win_width,win_height))

packman = Player('image/Pirat.png', 3, win_height - 90, 80, 85, 0, 0)
final_sprite = GameSprite('image/Pirat.png', win_width/2-100/2, win_height/2-100/2, 100, 100)

bullets_left = sprite.Group()
bullets_right = sprite.Group()

strike = 0
run = True

money = 0
murder = 0
open_shop = False
buy=False
font.init()
f1 = font.SysFont('monospaced', 80)

global mouse_pos
mouse_pos = 0
click = 0
while run:
    time.delay(15)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_a:
                direction = "left"
                packman.x_speed = -3
            elif e.key == K_d:
                direction = "right"
                packman.x_speed = 3
            elif e.key == K_w:
                packman.y_speed = -3
            elif e.key == K_s:
                packman.y_speed = 3
            
            elif e.key == K_SPACE:
                packman.fire(direction)
                strike+=1 
            elif e.key ==K_f:
                open_shop = True
            elif e.key == K_1:
                buy=True       
            elif e.key == K_c:
                open_shop = False
                background = transform.scale(image.load('image/cave.png'), (win_width, win_height))
                window.blit(background,(0,0))
                
        elif e.type == KEYUP:
            if e.key == K_a:
                packman.x_speed = 0
            elif e.key == K_d:
                packman.x_speed = 0 
            elif e.key == K_w:
                packman.y_speed = 0
            elif e.key == K_s:
                packman.y_speed = 0
        elif e.type == MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()
            clicked_button = check_button_click(mouse_pos)
        
            if clicked_button:
                if clicked_button.text == "Play":
                    print(clicked_button.text)
                    show_levels = 1
                            
                if clicked_button.text == "Settings":
                    print(clicked_button.text)
                    
                if clicked_button.text == "Exit":
                    print(clicked_button.text)
                    quit()
        
        elif in_level == 0:
            window.blit(back,(0,0))
            if show_levels == 0:
                draw_buttons()
                
            elif show_levels == 1:
                draw_buttons_level()
                background, barriers, monsters, coins, shops, show_levels, in_level = choose_level()
                  
        elif in_level :
            window.blit(background,(0,0))
            packman.update()
            packman.reset()
            
            coins.draw(window)
            shops.draw(window)
            barriers.draw(window)
            monsters.draw(window)            

            bullets_left.draw(window)
            bullets_right.draw(window)
            
            win = f1.render(str(money),True,(59, 58, 120))
            window.blit(win,(1250,700))   
                
            killl = f1.render(str(murder),True,(59, 58, 120))
            window.blit(killl,(1290,130))
            
            bullets_left.update("left")
            bullets_right.update("right")

            kil = sprite.groupcollide(monsters, bullets_left, True, True)
            kil_1 = sprite.groupcollide(monsters, bullets_right, True, True)
                        
            sprite.groupcollide(bullets_left, barriers, True, False)
            sprite.groupcollide(bullets_right, barriers, True, False)

            hits = sprite.groupcollide(bullets_left, coins, True, True)
            hits_1 = sprite.groupcollide(bullets_right, coins, True, True)
            
            if hits or hits_1:
                money+=1#Лічильник монет
                print(money)
            if kil or kil_1:
                murder+=1#Лічильник вбивств
                print(murder)

            if sprite.spritecollide(packman, monsters, False):
                finish = True
                img = transform.scale(image.load("image/lose.png"),(win_width,win_height))
                death = img.get_width() // img.get_height()   
                window.blit(img, (0, 0))
                choose_display = 0
            
            if len(monsters) == 0:
                final_sprite.reset()
                if sprite.collide_rect(packman, final_sprite):
                    finish = True
                    img = transform.scale(image.load("image/win.png"),(win_width,win_height))
                    window.blit(img, (0, 0))

            if sprite.spritecollide(packman, shops, False) and open_shop == True:
                imge = transform.scale(image.load("image/shop.jpg"),(win_width,win_height))
                window.blit(imge, (0, 0))
                ware = sprite.Group()

                pick = GameSprite('image/shop/pick.png', 100,230, 200,200)
                mapp = GameSprite('image/shop/map.png', 550,230, 200,200)
                dig = GameSprite('image/shop/dig.png', 1000,230, 200,200)
                    
                ware.add(pick)
                ware.add(mapp)
                ware.add(dig)

                ware.draw(window)
                if buy == True and money>=1: 
                    shop_message = "ви купили кирку"
                    show = f1.render(shop_message,True,(59, 58, 120))
                    window.blit(show,(300,600))
                    buy=False

    display.update()