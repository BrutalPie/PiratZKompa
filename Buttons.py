import pygame

pygame.init()

global win_width 
global win_height
win_info = pygame.display.Info()
win_width = win_info.current_w
win_height = win_info.current_h


global window
window = pygame.display.set_mode((win_width, win_height))