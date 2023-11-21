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
        return self.clicked

def check_button_click(mouse_pos):
    for button in buttons:
        if button.check_click(mouse_pos):
            print(button.text)
            return button
 
def check_button_click_level(mouse_pos):
    for t in buttons_chose_level:
        if t.check_click(mouse_pos):
            
            return t.text

def draw_buttons():
    for i in buttons:
        i.draw(window)

def draw_buttons_level():
    for t in buttons_chose_level:
        t.draw(window)


# Создаем несколько кнопок и добавляем их в список
buttons.append(Button("Play", 100, 100, 200, 50))
buttons.append(Button("Settings", 100, 200, 200, 50))
buttons.append(Button("Exit", 100, 300, 200, 50))

buttons_chose_level.append(Button("1", 450, 100, 100, 50))
buttons_chose_level.append(Button("2", 650, 100, 100, 50))
buttons_chose_level.append(Button("3", 850, 100, 100, 50))