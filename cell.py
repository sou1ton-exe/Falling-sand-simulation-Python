import pygame as pg
from consts_for_sand import *


class Cell:
    def __init__(self, size, state, x, y):
        self.size = size
        self.state = state
        self.x = x
        self.y = y
    
    def Draw(self, main_window):
        rect = pg.Rect(self.x, self.y, self.size, self.size)
        if self.state == 1: pg.draw.rect(main_window, ORANGE, rect)
        else: pg.draw.rect(main_window, BLACK, rect)