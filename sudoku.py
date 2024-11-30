# main file
import pygame

def main():
    # setup
    pygame.init()
    WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600  # could be anything, just make sure it's divisible by 3
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    display_surface.fill('white')
    pygame.display.set_caption("Sudoku")
    running = True  # bool for if game is running
    difficulty = None # 1 = easy, 2 = medium, 3 = hard

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
    easy_rect = pygame.Rect(100, 350, 100, 50)
    medium_rect = pygame.Rect(250, 350, 100, 50)
    hard_rect = pygame.Rect(400, 350, 100, 50)

    # draw text and recr to surface
    display_surface.blit(title_surf, (50,90))
    display_surface.blit(instruction_surf, (110, 250))
    pygame.draw.rect(display_surface, "orange", easy_rect)
    pygame.draw.rect(display_surface, "orange", medium_rect)
    pygame.draw.rect(display_surface, "orange", hard_rect)

    display_surface.blit(easy_text, (120, 365))
    display_surface.blit(medium_text, (257, 365))
    display_surface.blit(hard_text, (420, 365))
    #

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # difficulty selector
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_rect.collidepoint(mouse_pos):
                    difficulty = 1
                elif medium_rect.collidepoint(mouse_pos):
                    difficulty = 2
                elif hard_rect.collidepoint(mouse_pos):
                    difficulty = 3
        
        # just for testing
        print(difficulty)

        # update screen 
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()