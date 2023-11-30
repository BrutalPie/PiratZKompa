import pygame
from pygame import draw, font, Rect
from Main import win_width, win_height, window

pygame.init()
#
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#створення двох списків кнопок
global buttons
#головне меню
buttons = []
#меню вибору рівнів
buttons_chose_level = []
#класс кнопок для створення, та обробки кнопок
class Button:
    def __init__(self, text, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.text = text
        self.font = font.Font(None, 36)
        self.clicked = False
    #функція відрисовки кнопок
    def draw(self, window):
        draw.rect(window, BLACK, self.rect)
        text = self.font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        window.blit(text, text_rect)
    #функція перевірки натиску на кнопку
    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.clicked = True
        else:
            self.clicked = False
        return self.clicked
#функція перевірки натиску на кнопку головного меню
def check_button_click(mouse_pos):
    for button in buttons:
        if button.check_click(mouse_pos):
            print(button.text)
            return button
 #функція перевірки натиску на кнопку вибору рівня
def check_button_click_level(mouse_pos):
    for t in buttons_chose_level:
        if t.check_click(mouse_pos):
            
            return t.text
#функція відрисовки кнопок головного меню
def draw_buttons():
    for i in buttons:
        i.draw(window)
#функція відрисовки кнопок меню вибору рівня
def draw_buttons_level():
    for t in buttons_chose_level:
        t.draw(window)


#створення та додавання кнопок до списків
buttons.append(Button("Play", 100, 100, 200, 50))
buttons.append(Button("Settings", 100, 200, 200, 50))
buttons.append(Button("Exit", 100, 300, 200, 50))

buttons_chose_level.append(Button("1-level", 450, 200, 150, 80))
buttons_chose_level.append(Button("2-level", 650, 200, 150, 80))
buttons_chose_level.append(Button("3-level", 850, 200, 150, 80))