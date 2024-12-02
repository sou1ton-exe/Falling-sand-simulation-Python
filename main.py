import pygame as pg
import random
from consts_for_sand import *
from cell import Cell

is_play = True
main_window = pg.display.set_mode(SIZE)
time = pg.time.Clock()
last_ticks = pg.time.get_ticks()

matrix_of_cells = [[Cell(SIZE_OF_CELLS, random.randint(0,1), j*SIZE_OF_CELLS, i*SIZE_OF_CELLS) for j in range(CELL_CONST)] for i in range(CELL_CONST)]

def Falling():
    global matrix_of_cells
    
    for i in range(1, len(matrix_of_cells)):
        for j in range(len(matrix_of_cells[i])):
            if matrix_of_cells[i][j].state == 0 and matrix_of_cells[i-1][j].state == 1: 
                matrix_of_cells[i][j].state = 1
                matrix_of_cells[i-1][j].state = 0

def Slide():
    global matrix_of_cells
    
    for i in range(len(matrix_of_cells)):
        for j in range(len(matrix_of_cells[i])):  
            
            if i-1 >= 0 and j+1 <= len(matrix_of_cells)-1:
                if matrix_of_cells[i][j].state == 0 and matrix_of_cells[i-1][j+1].state == 1 and random.randint(1,3) == 3:
                    matrix_of_cells[i][j].state = 1
                    matrix_of_cells[i-1][j+1].state = 0
            
            if i-1 >= 0 and j-1 >= 0:
                if matrix_of_cells[i][j].state == 0 and matrix_of_cells[i-1][j-1].state == 1 and random.randint(1,3) == 3:
                    matrix_of_cells[i][j].state = 1
                    matrix_of_cells[i-1][j-1].state = 0

while is_play:
    Falling()
    Slide()
    
    objectives = pg.event.get()
    
    for i in range(len(objectives)):
        if objectives[i].type == pg.QUIT:
            is_play = False
            break
    
    main_window.fill(BLACK)
    
    for i in range(CELL_CONST):
        for j in range(CELL_CONST):
            matrix_of_cells[i][j].Draw(main_window)
    
    pg.display.update()

    time.tick(FPS)