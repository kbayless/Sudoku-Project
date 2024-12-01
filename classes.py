# file for classes
import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        #screen is the pygame display
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        cell_size = 60
        x = self.col * cell_size
        y = self.row * cell_size
        rect_color = (255, 0, 0) if self.selected else (0, 0, 0)
        pygame.draw.rect(self.screen, rect_color, (x, y, cell_size, cell_size), 2)

        if self.value != 0:
            font = pygame.font.Font(None, 40)
            text = font.render(str(self.value), True, 'black')
            self.screen.blit(text, (x + 20, y + 10))

class Board:
    def __init__(self, width, height, screen, board_data):
        self.width = width
        self.height = height
        self.screen = screen
        self.board_data = board_data
        self.cells = [
            [Cell(board_data[row][col], row, col, screen) for col in range(9)]
            for row in range(9)
        ]
        self.selected_cell = None

    def draw(self):
        for i in range(10):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, "black", (0, i * 60), (540, i * 60), line_width)
            pygame.draw.line(self.screen, "black", (i * 60, 0), (i * 60, 540), line_width)

        for row in self.cells:
            for cell in row:
                cell.draw()

    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):
        if 0 <= x <= 540 and 0 <= y <= 540:
            return y // 60, x // 60
        return None

