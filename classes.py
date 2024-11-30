# file for classes
import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.position = f'[{row}][{col}]'
        #screen is the pygame display
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value
        self.screen.display.flip()

    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(30, 30, 60, 60))
        pygame.
        pygame.display.flip()

class Board:
    pass