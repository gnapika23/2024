import pygame
import sys
from game import Game2048

# Pygame setup
pygame.init()

# Constants
SIZE = 4
TILE_SIZE = 100
PADDING = 10
BOARD_SIZE = SIZE * TILE_SIZE + (SIZE + 1) * PADDING
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
FONT = pygame.font.SysFont("arial", 40)

def draw_board(screen, game):
    screen.fill(BACKGROUND_COLOR)
    for r in range(SIZE):
        for c in range(SIZE):
            value = game.board[r][c]
            color = TILE_COLORS.get(value, (60, 58, 50))
            rect = pygame.Rect(c * TILE_SIZE + (c + 1) * PADDING,
                               r * TILE_SIZE + (r + 1) * PADDING,
                               TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, color, rect)
            if value != 0:
                text = FONT.render(str(value), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    
    # Display score
    score_text = FONT.render(f'Score: {game.score}', True, (0, 0, 0))
    screen.blit(score_text, (10, BOARD_SIZE - 50))
    
    pygame.display.update()

def main():
    screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
    pygame.display.set_caption("2048")
    game = Game2048()
    
    draw_board(screen, game)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.move(3)
                elif event.key == pygame.K_LEFT:
                    game.move(0)
                elif event.key == pygame.K_DOWN:
                    game.move(1)
                elif event.key == pygame.K_RIGHT:
                    game.move(2)
                draw_board(screen, game)
                if game.is_game_over():
                    print("Game Over")
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
