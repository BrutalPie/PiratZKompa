'''from pygame import draw, font, Rect
from Main import win_width, win_height, window

global button_rect
button_rect = Rect(300, 250, 200, 100)
# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font.init()
global button_font
button_font = font.Font(None, 36)

def draw_button(window, button_rect,button_font):
    draw.rect(window, BLACK, button_rect)
    text = button_font.render("Кнопка", True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    window.blit(text, text_rect)'''

import pygame
from pygame import draw, font, Rect
from Main import win_width, win_height, window

# Инициализация Pygame
pygame.init()

# кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создаем список кнопок
global buttons
buttons = []
buttons_chose_level = []
# Создаем класс для кнопок
class Button:
    def __init__(self, text, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.text = text
        self.font = font.Font(None, 36)
        self.clicked = False
    
    def draw(self, window):
        draw.rect(window, BLACK, self.rect)
        text = self.font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        window.blit(text, text_rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.clicked = True
        else:
            self.clicked = False
            return False
        return self.clicked
# Создаем несколько кнопок и добавляем их в список
buttons.append(Button("Play", 100, 100, 200, 50))
buttons.append(Button("Settings", 100, 200, 200, 50))
buttons.append(Button("Exit", 100, 300, 200, 50))

buttons_chose_level.append(Button("1", 50, 100, 100, 50))
buttons_chose_level.append(Button("2", 50, 100, 100, 50))
buttons_chose_level.append(Button("3", 50, 100, 100, 50))

def check_button_click(mouse_pos,):
    for button in buttons_chose_level:
        if button.check_click(mouse_pos):
            return button
    for button in buttons:
        if button.check_click(mouse_pos):
            return button
    return None

# Этот код проверит, какая кнопка была нажата, и вернет соответствующий объект Button

# Далее вы можете выполнить какое-либо действие на основе нажатой кнопки

def draw_buttons():
    for button in buttons:
        button.draw(window)

def draw_buttons_level():
    for button in buttons_chose_level:
        button.draw(window)

