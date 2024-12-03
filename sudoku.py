# main file
import pygame
from sudoku_generator import generate_sudoku
from classes import Board

def main():
    # setup
    pygame.init()
    WINDOW_WIDTH, WINDOW_HEIGHT = 540, 600  # could be anything, just make sure it's divisible by 3
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    display_surface.fill('white')
    pygame.display.set_caption("Sudoku")
    running = True  # bool for if game is running
    game_over = False
    game_won = False
    difficulty = None
    game_started = False
    game_over_screen = False
    board = None

    # drawing startmenu
    # creating fonts/surfs to draw on display_surf
    title_font = pygame.font.Font(None, 75)
    title_surf = title_font.render("Welcome to Sudoku", True, 'black')

    instruction_font = pygame.font.Font(None, 55)
    instruction_surf = instruction_font.render("Select Game Mode:", True, 'black')

    text_font = pygame.font.Font(None, 30)
    easy_text = text_font.render("EASY", True, "white")
    medium_text = text_font.render("MEDIUM", True, "white")
    hard_text = text_font.render("HARD", True, "white")

    # create rect for difficulty selectors
    easy_rect = pygame.Rect(70, 350, 100, 50)
    medium_rect = pygame.Rect(220, 350, 100, 50)
    hard_rect = pygame.Rect(370, 350, 100, 50)

    # draw text and recr to surface
    display_surface.blit(title_surf, (20, 90))
    display_surface.blit(instruction_surf, (90, 250))
    pygame.draw.rect(display_surface, "orange", easy_rect)
    pygame.draw.rect(display_surface, "orange", medium_rect)
    pygame.draw.rect(display_surface, "orange", hard_rect)

    display_surface.blit(easy_text, (90, 365))
    display_surface.blit(medium_text, (227, 365))
    display_surface.blit(hard_text, (390, 365))
    #

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_over:

                # difficulty selector
                if not game_started:
                    if event.type == pygame.MOUSEBUTTONUP:
                        mouse_pos = pygame.mouse.get_pos()
                        if easy_rect.collidepoint(mouse_pos):
                            difficulty = 30
                        elif medium_rect.collidepoint(mouse_pos):
                            difficulty = 40
                        elif hard_rect.collidepoint(mouse_pos):
                            difficulty = 50

                        # if difficulty selected => create board
                        if difficulty:
                            solved_board, board = generate_sudoku(9, difficulty)
                            game_board = board
                            board = Board(WINDOW_WIDTH, WINDOW_HEIGHT, display_surface, game_board)
                            game_started = True

                            # draw board
                            display_surface.fill('white')
                            board.draw()

                    elif game_started:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False

                # user input
                if game_started and (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN):
                    # mouse input
                    if event.type == pygame.MOUSEBUTTONUP:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        selected_row, selected_col = board.click(mouse_x, mouse_y)

                    # keyboard input
                    if event.type == pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_LEFT:
                                if selected_col > 0: selected_col -= 1
                            case pygame.K_RIGHT:
                                if selected_col < 8: selected_col += 1
                            case pygame.K_UP:
                                if selected_row > 0: selected_row -= 1
                            case pygame.K_DOWN:
                                if selected_row < 8: selected_row += 1

                    # select cell
                    if selected_col != None and selected_row != None:
                        board.select(selected_row, selected_col)

                    # this will set each cell as either user inputted or not when its initially selected
                    if board.selected_cell.value != 0 and board.selected_cell.user_inputted is None:
                        board.selected_cell.user_inputted = False
                    elif board.selected_cell.value == 0 and board.selected_cell.user_inputted is None:
                        board.selected_cell.user_inputted = True

                    # sketch numbers
                    if event.type == pygame.KEYDOWN:
                        try:
                            num = int(pygame.key.name(event.key))
                            if num > 0:
                                board.sketch(num)
                        except ValueError:
                            pass

                    # enter numbers
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and board.selected_cell.sketched_value:
                            board.selected_cell.value = board.selected_cell.sketched_value
                            board.update_board()

                    #remove number (clear cell)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            board.clear()

                    # check if board is full
                    if board.is_full():
                        if board.board_data == solved_board:
                            game_won = True
                            game_over = True
                        else:
                            game_over = True

                    # draw board
                    display_surface.fill('white')
                    board.draw()
            else:
                if not game_over_screen:
                    display_surface.fill('white')
                    font = pygame.font.Font(None, 75)
                    if game_won:
                        message = font.render('Game won!', True, 'black')
                        exit_font = pygame.font.Font(None, 50)
                        exit_text = exit_font.render("Exit", True, 'white')
                        exit_rect = pygame.Rect(195, 350, 150, 60)
                        pygame.draw.rect(display_surface, 'orange', exit_rect)
                        display_surface.blit(exit_text, (237, 365))
                    else:
                        message = font.render('Game over :(', True, 'black')
                        restart_font = pygame.font.Font(None, 50)
                        restart_text = restart_font.render("Restart", True, 'white')
                        restart_rect = pygame.Rect(195, 350, 150, 60)
                        pygame.draw.rect(display_surface, 'orange', restart_rect)
                        display_surface.blit(restart_text, (211, 365))
                    message_rect = message.get_rect(center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 120))
                    display_surface.blit(message, message_rect)
                    pygame.display.flip()
                    game_over_screen = True

                #handling restart / exit cases
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    if game_won:
                        if exit_rect.collidepoint(mouse_pos):
                            pygame.quit()
                            exit()
                    else:
                        if restart_rect.collidepoint(mouse_pos):
                            main()

        # update screen
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
