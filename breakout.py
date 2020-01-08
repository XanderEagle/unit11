import pygame, sys
from pygame.locals import *


def main():
    # Constants that will be used in the program
    application_width = 400
    application_height = 600
    paddle_y_offset = 30
    bricks_per_row = 10
    brick_sep = 4  # The space between each brick
    brick_y_offset = 70
    brick_width = (application_width - (bricks_per_row -1) * brick_sep) / bricks_per_row
    brick_height = 8
    paddle_width = 60
    paddle_height = 10
    radius_of_ball = 10
    num_turns = 3

    # Sets up the colors
    red = (255, 0, 0)
    orange = (255, 165, 0)
    yellow = (255, 255, 0)
    green =(0, 255, 0)
    cyan = (0, 255, 255)
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)

    main_surface = pygame.display.set_mode((application_width, application_height), 0, 32)
    main.surface.fill(255, 255, 255)
    x_pos = brick_sep
    y_pos = brick_y_offset




    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()

main()
