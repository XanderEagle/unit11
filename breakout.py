import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball


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

    bricks_group = pygame.sprite.Group()

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)

    main_surface = pygame.display.set_mode((application_width, application_height), 0, 32)
    main_surface.fill((255, 255, 255))
    x_pos = brick_sep
    y_pos = brick_y_offset

    my_paddle = paddle.Paddle(main_surface, (black), (paddle_width), (paddle_height))
    my_paddle.rect.x = 200
    my_paddle.rect.y = 570
    main_surface.blit(my_paddle.image, my_paddle.rect)

    my_ball = ball.Ball((black), application_width, application_height, radius_of_ball)
    my_ball.rect.x = 200
    my_ball.rect.y = 300
    main_surface.blit(my_ball.image, my_ball.rect)

    for x in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (red))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (red))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (orange))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (orange))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (yellow))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (yellow))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (green))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (green))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (cyan))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (cyan))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width
    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)

    while True:
        main_surface.fill(white)
        for a_brick in bricks_group:
            main_surface.blit(a_brick.image, a_brick.rect)
        my_paddle.move(pygame.mouse.get_pos())
        main_surface.blit(my_paddle.image, my_paddle.rect)
        my_ball.move()
        main_surface.blit(my_ball.image, my_ball.rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()


main()
