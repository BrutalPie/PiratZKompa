import pygame
from Main import *
from MenuButton import *


pygame.init()

class Player(GameSprite):
    #метод, у якому реалізовано управління спрайтом за кнопками стрілочкам клавіатури
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    ''' переміщає персонажа, застосовуючи поточну горизонтальну та вертикальну швидкість'''
    def update(self):  
        # Спершу рух по горизонталі
        if packman.rect.x <= win_width-60 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: # йдемо праворуч, правий край персонажа - впритул до лівого краю стіни
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) # якщо торкнулися відразу кількох, то правий край - мінімальний із можливих
        elif self.x_speed < 0: # йдемо ліворуч, ставимо лівий край персонажа впритул до правого краю стіни
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) # якщо торкнулися кількох стін, то лівий край - максимальний
        if packman.rect.y <= win_height-85 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: # йдемо вниз
            for p in platforms_touched:
                # Перевіряємо, яка з платформ знизу найвища, вирівнюємося по ній, запам'ятовуємо її як свою опору:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: # йдемо вгору
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom) # вирівнюємо верхній край по нижніх краях стінок, на які наїхали
                    
    # метод "постріл" (використовуємо місце гравця, щоб створити там кулю)
    def fire(self,direction):
        bullet = Bullet('image/bullet.png', self.rect.centerx, self.rect.top+40, 15, 15, 15)
        if direction == "left":
            bullets_left.add(bullet)
        elif direction == "right":
            bullets_right.add(bullet)
#клас спрайту-ворога
#Enemy

# клас спрайту-кулі
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    #рух ворога


    def update(self,direction):
        if direction == "left":
            self.rect.x -= self.speed
            # зникає, якщо дійде до краю екрана
            if self.rect.x < 0:
                self.kill()
        elif direction == "right":
            self.rect.x += self.speed
            # зникає, якщо дійде до краю екрана
            if self.rect.x > win_width:
                self.kill()

choose_display = 0
display.set_caption("Labirint")
#back = ret_back(choose_display)
back = transform.scale(image.load('image/island.png'),(win_width,win_height))

packman = Player('image/Pirat.png', 3, win_height - 90, 80, 85, 0, 0)
final_sprite = GameSprite('image/Pirat.png', win_width/2-100/2, win_height/2-100/2, 100, 100)

strike = 0

finish = False
run = True
#coins = sprite.Group()
#shops = sprite.Group()'''

#coin1 = GameSprite('image/coin.png', 330,60, 50,50)
#coin2 = GameSprite('image/coin.png', 990,530, 50,50)

#shope = GameSprite('image/shop.png', 930,430, 50,50)

#windower = display_Set()



#coins.add(coin1)
#coins.add(coin2)

#shops.add(shope)
#money = 0
##murder = 0
#sh=0


#font.init()
#f1 = font.SysFont('monospaced', 80)
#open_shop = False
#y=False
#show=0
#buy=False
#Розташування кнопок і самі кнопки
#button_rect = Rect(300, 250, 200, 100)
click = 0
while run:

    time.delay(5)
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

            #elif e.key ==K_f:
                #open_shop = True
            #elif e.key == K_1:
                #buy=True
                    
                    
            #elif e.key == K_c:
                #open_shop = False
                #window.blit(back,(0,0))
                
            
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
            if e.button == 1:
                mouse_pos = mouse.get_pos()  # Получаем позицию мыши при клике
                
                for button in buttons:
                    if button.check_click(mouse_pos) == True:
                        choose_display = 1
                        print("Левая кнопка мыши нажата в точке", mouse_pos)
                    elif button.check_click(mouse_pos) == False:
                        choose_display = 0
                        print("Клік не потрапив в зону кнопок")
                        
                

#перевірка, що гра ще не завершена
    
    if choose_display == 0:
        window.blit(back,(0,0))
        finish = True
        draw_buttons()
    else:
        if finish == False and choose_display>0:
            from level_1 import *
            back = transform.scale(image.load('image/cave.png'),(win_width,win_height))
            barriers = ret_barriers()
            monsters = ret_monsters()
            #win = f1.render(str(money),True,(59, 58, 120))
            #window.blit(win,(1250,700))#Лічильник монет
            
            #killl = f1.render(str(murder),True,(59, 58, 120))
            #window.blit(killl,(1290,130))

            #запускаємо рухи спрайтів
            packman.update()
            bullets_left.update("left")
            bullets_right.update("right")
            
            #оновлюємо їх у новому місці при кожній ітерації циклу
            packman.reset()
            #рисуємо стіни 2
            bullets_left.draw(window)
            bullets_right.draw(window)
            barriers.draw(window)


        # kil = sprite.groupcollide(monsters, bullets_left, True, True)
            #kil_1 = sprite.groupcollide(monsters, bullets_right, True, True)
        

            monsters.draw(window)
            sprite.groupcollide(bullets_left, barriers, True, False)
            sprite.groupcollide(bullets_right, barriers, True, False)

            #coins.draw(window)
            #shops.draw(window)

            #hits = sprite.groupcollide(bullets_left, coins, True, True)
            #hits_1 = sprite.groupcollide(bullets_right, coins, True, True)
        
            #if hits or hits_1:
            #   money+=1#Лічильник монет

            #if kil or kil_1:
                #murder+=1#Лічильник вбивств

            #Перевірка зіткнення героя з ворогом та стінами
            if sprite.spritecollide(packman, monsters, False):
                finish = True
                # обчислюємо ставлення
                img = transform.scale(image.load("image/lose.png"),(win_width,win_height))
                d = img.get_width() // img.get_height()
                
                window.blit(img, (0, 0))
                
        
            if len(monsters) == 0:
                final_sprite.reset()
                if sprite.collide_rect(packman, final_sprite):
                    finish = True
                    img = transform.scale(image.load("image/win.png"),(win_width,win_height))
                    window.blit(img, (0, 0))

            #if sprite.spritecollide(packman, shops, False) and open_shop == True:
            #   imge = transform.scale(image.load("image/shop.back.jpg"),(1368,768))
            #  window.blit(imge, (0, 0))
            # ware = sprite.Group()

                #pick = GameSprite('image/shop/pick.png', 100,230, 200,200)
                #mapp = GameSprite('image/shop/map.png', 550,230, 200,200)
                #dig = GameSprite('image/shop/dig.png', 1000,230, 200,200)
                
                #ware.add(pick)
                #ware.add(mapp)
                #ware.add(dig)

                #ware.draw(window)
                #if buy == True: 
                #   shop_message = "ви купили кирку"
                #  show = f1.render(shop_message,True,(59, 58, 120))
                # window.blit(show,(300,600))
                #buy=False'''
                

        display.update()