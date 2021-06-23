import pygame
import numpy as np

pygame.init()

FPS = 144
BACKGROUND_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 23
SPACE = 50
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
WINDOW.fill(BACKGROUND_COLOR)

BOARD = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines():
    pygame.draw.line(WINDOW, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(WINDOW, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(WINDOW, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(WINDOW, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if BOARD[row][col] == 1:
                pygame.draw.circle(WINDOW, CIRCLE_COLOR, (col * 200 + 100, row * 200 + 100), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif BOARD[row][col] == 2:
                pygame.draw.line(WINDOW, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(WINDOW, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)


def mark_square(row, col, player):
    BOARD[row][col] = player


def available_square(row, col):
    return BOARD[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if BOARD[row][col] == 0:
                return False
    return True


def check_win(player):
    for col in range(BOARD_COLS):
        if BOARD[0][col] == player and BOARD[1][col] == player and BOARD[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if BOARD[row][0] == player and BOARD[row][1] == player and BOARD[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    if BOARD[0][2] == player and BOARD[1][1] == player and BOARD[2][0] == player:
        draw_asc_diagonal_winning_line(player)
        return True

    if BOARD[0][0] == player and BOARD[1][1] == player and BOARD[2][2] == player:
        draw_desc_diagonal_winning_line(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    position_x = col * 200 + 100
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(WINDOW, color, (position_x, 15), (position_x, WINDOW_HEIGHT - 15), 8)


def draw_horizontal_winning_line(row, player):
    position_y = row * 200 + 100
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(WINDOW, color, (15, position_y), (WINDOW_WIDTH - 15, position_y), 8)


def draw_asc_diagonal_winning_line(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(WINDOW, color, (15, WINDOW_HEIGHT - 15), (WINDOW_WIDTH - 15, 15), 8)


def draw_desc_diagonal_winning_line(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(WINDOW, color, (15, 15), (WINDOW_WIDTH - 15, WINDOW_HEIGHT - 15), 8)


def restart():
    WINDOW.fill(BACKGROUND_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            BOARD[row][col] = 0


draw_lines()

run = True
clock = pygame.time.Clock()
player = 1
game_over = False

while run:
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            clicked_row = int(mouse_y // 200)
            clicked_col = int(mouse_x // 200)
            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_over = False
                restart()
