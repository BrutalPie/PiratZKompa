import pygame
from Main import *
from MenuButton import *
import time
pygame.init()
start_time = time.time()

direction = "right"
clock = pygame.time.Clock() #оновлення кадрів(метод бібліотеки)
#класс головного героя, який приймає значення(self, зображення героя, координата-x, координата-y, розмір-x, розмір-y, x-швидкість гравця, y-швидкість гравця)
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
#перевірка зіткнення головного героя з краями екрану
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
#постріл, створення пулі та визначення її напряму руху(ліво,право)
    def fire(self,direction):
        bullet = Bullet('image/bullet.png', self.rect.centerx, self.rect.top+40, 15, 15, 15)
        if direction == "left":
            bullets_left.add(bullet)
        elif direction == "right":
            bullets_right.add(bullet)
#класс головного героя, який приймає значення(self, зображення пулі, координата-x, координата-y, розмір-x, розмір-y, x-швидкість, y-швидкість)
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
#перевірка виходу пулі за межі єкрану, та видалення пулі при виході за ці межі
    def update(self,direction):
        if direction == "left":
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.kill()
        elif direction == "right":
            self.rect.x += self.speed
            if self.rect.x > win_width:
                self.kill()
#визначення основних змінних для імпорту данних рівня
show_levels = 0
in_level = False
background = None
barriers = None
monsters = None
coins = None
shops =None
mouse_pos = 0
#вибір рівня, та імпорт даних одного з можливих рівнів, та присвоєння цих данних в змінним вище
def choose_level():
    global background, barriers, monsters, coins, shops, show_levels, in_level
    clicked_button_level = check_button_click_level(mouse_pos)
    if clicked_button_level == "1-level": 
        import level_1
        background = transform.scale(image.load('image/cave.png'), (win_width, win_height))
        barriers = level_1.ret_barriers()
        monsters = level_1.ret_monsters()
        coins = level_1.ret_coin()
        shops = level_1.ret_shop()
        show_levels = 2
        in_level = True
        
    if clicked_button_level == "2-level": 
        import level_2
        background = transform.scale(image.load('image/cave.png'), (win_width, win_height))
        barriers = level_2.ret_barriers()
        monsters = level_2.ret_monsters()
        coins = level_2.ret_coin()
        shops = level_2.ret_shop()
        show_levels = 2
        in_level = True

    if clicked_button_level == "3-level": 
        import level_3
        background = transform.scale(image.load('image/cave.png'), (win_width, win_height))
        barriers = level_3.ret_barriers()
        monsters = level_3.ret_monsters()
        coins = level_3.ret_coin()
        shops = level_3.ret_shop()
        show_levels = 2
        in_level = True
    
    return background, barriers, monsters, coins, shops, show_levels, in_level
#назва гри при відображенні в панелі задач
display.set_caption("PiratesGame")
#встановлення основного фону(головне меню), та заливка ним екрану(win_width,win_height)
back = transform.scale(image.load('image/island.png'),(win_width,win_height))
#змінна головного героя, для визначення його параметрів
packman = 0
#створення фінального спрайту
final_sprite = GameSprite('image/Pirat.png', win_width/2-100/2, win_height/2-100/2, 100, 100)
#групи пулей
bullets_left = sprite.Group()
bullets_right = sprite.Group()
#змінна для перевірки попадання в монстра
strike = 0
#змінні(лічильник коштів(гаманець),лічильник вбивств, перевірка відкриття та купівлі в магазині)
money = 0
murder = 0
open_shop = False
buy=False
#метод для визначення розміру та стилю тексту
font.init()
f1 = font.SysFont('monospaced', 80)
#змінна для перевірки натискання ESCAPE(вихід)
click_escape = 0
# поки True, гра працює
run = True
while run:
    #частота оновлення екрану
    clock.tick(60)
    #переірка взаємодій в грі(event.get)
    for e in event.get():
        #перевірка виходу з гри
        if e.type == QUIT:
            run = False
        #перевірка натиску клавіш
        elif e.type == KEYDOWN:
            #перевірка натиску клавіші a, та рух вліво на 3 пікселі
            if e.key == K_a:
                direction = "left"
                packman.x_speed = -3
            #перевірка натиску клавіші d, та рух вправо на 3 пікселі
            elif e.key == K_d:
                direction = "right"
                packman.x_speed = 3
                pygame.key.set_repeat(10,10)
            #перевірка натиску клавіші w, та рух вверх на 3 пікселі
            elif e.key == K_w:
                packman.y_speed = -3
                
            #перевірка натиску клавіші s, та рух вниз на 3 пікселі
            elif e.key == K_s:
                packman.y_speed = 3
            #перевірка натиску клавіші Escape, вихід в меню вибору рівнів
            elif e.key == K_ESCAPE:
                in_level = False
                click_escape += 1
                show_levels = 1
                #при повторному натиску Escape вихід в головне меню 
                if show_levels ==1 and click_escape == 2:
                    print("out menu")
                    show_levels = 0
                    click_escape = 0
            #при натиску space(пробіл)- постріл
            elif e.key == K_SPACE:
                packman.fire(direction)
                strike+=1 
            #перевірка натиску f, змінні відкриття магазину змінюються на True(магазин відкрито)
            elif e.key ==K_f:
                open_shop = True
            #Якщо магазин відкрито, і натиснуто(1,2 або 3)відбувається купівля конкретного предмету
            if open_shop == True:
                if e.key == K_1:
                    buy=1
                elif e.key == K_2:
                    buy = 2
                elif e.key == K_3:
                    buy = 3                
                #закриття магазину натиском клавіші с та повернення до рівня
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
        #перевірка кліку лівої кнопки миші
        elif e.type == MOUSEBUTTONDOWN:
            #отримання позиції миші у місці кліку
            mouse_pos = mouse.get_pos()
            #присвоєння функцції з файлу MenuButton. Перевірка натиску однієї з кнопок у списку
            clicked_button = check_button_click(mouse_pos)
            #якщо натиснуто
            if clicked_button:
                #Play-грати
                if clicked_button.text == "Play":
                    print(clicked_button.text)
                    show_levels = 1
                #Settings-налаштування 
                if clicked_button.text == "Settings":
                    print(clicked_button.text)
                #Exit-вихід з гри
                if clicked_button.text == "Exit":
                    print(clicked_button.text)
                    quit()
        #перевірки чи користувач знаходиться в рівні при in_level == 0(не в рівні)
        elif in_level == 0:
            #заповнення вікна фоном заданим раніше, back
            window.blit(back,(0,0))
           #виводить кнопки головного меню на екран  
            if show_levels == 0:
                draw_buttons()
           #виводить кнопки вибору рівня на екран 
            elif show_levels == 1:
                murder = 0
                draw_buttons_level()
                packman = Player('image/Pirat.png', 3, win_height - 90, 80, 85, 0, 0)
                #підгружає обраний гравцем рівень
                background, barriers, monsters, coins, shops, show_levels, in_level = choose_level()
        #в рівні          
        elif in_level :
            #змінює задній фон локації на інший заданий
            window.blit(background,(0,0))
            #оновлення головного героя на екрані
            packman.update()
            #оновлення руху героя
            packman.reset()
            # відрисовка монет, магазину, сітн, та монстрів
            coins.draw(window)
            shops.draw(window)
            barriers.draw(window)
            monsters.draw(window)            
            #відрисовка руху куль на екрані
            bullets_left.draw(window)
            bullets_right.draw(window)
            #лічильник монет на екрані
            win = f1.render(str(money),True,(59, 58, 120))
            #відопраження лічильника монет у певній точці екрану
            window.blit(win,(1850,130))   
            #лічильник вбивств
            killl = f1.render(str(murder),True,(59, 58, 120))
            #відопраження лічильника вбивств у певній точці екрану
            window.blit(killl,(1697,130))
            #оновлення куль на екрані
            bullets_left.update("left")
            bullets_right.update("right")
            #перевірка зіткення пулі випущеної вліво з монстром
            kil = sprite.groupcollide(monsters, bullets_left, True, True)
            #перевірка зіткення пулі випущеної вправо з монстром
            kil_1 = sprite.groupcollide(monsters, bullets_right, True, True)
            #створення окремих груп зіткнень
            sprite.groupcollide(bullets_left, barriers, True, False)
            sprite.groupcollide(bullets_right, barriers, True, False)
            #перевірка зіткення пулі випущеної вліво з монетою
            hits = sprite.groupcollide(bullets_left, coins, True, True)
            #перевірка зіткення пулі випущеної вправо з монетою
            hits_1 = sprite.groupcollide(bullets_right, coins, True, True)
            #якщо зіткнення пулі з монетою, то
            if hits or hits_1:
                money+=1#Лічильник монет +1
                print(money)
            #якщо зіткнення пулі з монстром, то
            if kil or kil_1:
                murder+=1#Лічильник вбивств +1
                print(murder)
            #якщо відбулось зіткнення головного героя з монстром, то виводиться спрайт з 
            # надписом lose і відбувається повернення до головного меню
            if sprite.spritecollide(packman, monsters, False):
                finish = True
                img = transform.scale(image.load("image/lose.png"),(win_width,win_height))
                death = img.get_width() // img.get_height()   
                window.blit(img, (0, 0))
                show_levels = 0
                in_level = False
            #перевірка залишившихся монстрів
            if len(monsters) == 0:
                final_sprite.reset()
                #якщо монстрів не залишилось, то з'являється головний спрайт по центру екрана,
                #і при перетині спрайту головного героя і головного спрайту на екран виводиться 
                # напис win і гра повертає гравця до головного меню
                if sprite.collide_rect(packman, final_sprite):
                    finish = True
                    img = transform.scale(image.load("image/win.png"),(win_width,win_height))
                    window.blit(img, (0, 0))
                    show_levels = 0
                    in_level = False
            #при перетині спрайтів головного героя та магазину і натиснутій кнопці f 
            # відкривається магазин
            if sprite.spritecollide(packman, shops, False) and open_shop == True:
                imge = transform.scale(image.load("image/shop.jpg"),(win_width,win_height))
                window.blit(imge, (0, 0))
                ware = sprite.Group()
                #створення таких об'єктів, як: кирка, карта, лопата
                pick = GameSprite('image/shop/pick.png', 100,230, 200,200)
                mapp = GameSprite('image/shop/map.png', 550,230, 200,200)
                dig = GameSprite('image/shop/dig.png', 1000,230, 200,200)
                #додавання цих об'єктів у список
                ware.add(pick)
                ware.add(mapp)
                ware.add(dig)

                ware.draw(window)
                #якщо в гаманці більше чим 1 монета та була натиснута клавіша 1 то 
                # відбувається покупка кирки
                if buy == 1 and money>=1: 
                    shop_message = "ви купили кирку"
                    show = f1.render(shop_message,True,(59, 58, 120))
                    window.blit(show,(300,600))
                    buy=0
                    money-=1
                #якщо в гаманці більше чим 2 монети та була натиснута клавіша 2 то 
                # відбувається покупка карти
                if buy == 2 and money>=2:
                    shop_message = "ви купили карту"
                    show = f1.render(shop_message,True,(59, 58, 120))
                    window.blit(show,(300,600))
                    buy=False
                    money-=1
                #якщо в гаманці більше чим 1 монета та була натиснута клавіша 3 то 
                # відбувається покупка лопати
                if buy == 3 and money>=1:
                    shop_message = "ви купили лопату"
                    show = f1.render(shop_message,True,(59, 58, 120))
                    window.blit(show,(300,600))
                    buy=False
                    money-=1
    #оновлення сцени
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Программа виконана за {execution_time} секунд")
    display.update()