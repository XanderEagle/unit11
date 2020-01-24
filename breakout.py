# Xander Eagle
# January 24, 2020

# This program makes a star wars themed breakout game (YOU HAVE TO USE THE FORCE BECAUSE THE BALL IS HARD TO SEE)

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
    black = (0, 0, 0)
    white = (255, 255, 255)
    purple = (195, 47, 191)

    bricks_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()

    # makes the main surface
    main_surface = pygame.display.set_mode((application_width, application_height), 0, 32)
    main_surface.fill((0, 0, 0))
    background = pygame.image.load("revan.jpg")
    main_surface.blit(background, (0, 0))
    x_pos = brick_sep
    y_pos = brick_y_offset

    # makes the paddle
    my_paddle = paddle.Paddle(main_surface, (black), (paddle_width), (paddle_height))
    my_paddle.rect.x = 200
    my_paddle.rect.y = 570
    main_surface.blit(my_paddle.image, my_paddle.rect)
    paddle_group.add(my_paddle)

    # makes the ball
    my_ball = ball.Ball(white, application_width, application_height, radius_of_ball)
    my_ball.rect.x = 900
    my_ball.rect.y = 1000
    main_surface.blit(my_ball.image, my_ball.rect)
    pygame.display.update()

    # Makes the rows of bricks
    for x in range(bricks_per_row):
        my_brick = brick.Brick(brick_width, (brick_height), (red))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick(brick_width, (brick_height), (red))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (purple))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (purple))
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
        my_brick = brick.Brick((brick_width), (brick_height), (red))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (purple))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    x_pos = brick_sep
    y_pos = y_pos + brick_height + brick_sep

    for y in range(bricks_per_row):
        my_brick = brick.Brick((brick_width), (brick_height), (purple))
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
        my_brick = brick.Brick((brick_width), (brick_height), (red))
        my_brick.rect.x = x_pos
        my_brick.rect.y = y_pos
        bricks_group.add(my_brick)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + brick_sep + brick_width

    # loop that moves paddle and collides the ball and paddle as well as ends the game after 3 turns
    while True:
        main_surface.blit(background, (0, 0))
        for a_brick in bricks_group:
            main_surface.blit(a_brick.image, a_brick.rect)
        my_paddle.move(pygame.mouse.get_pos())
        my_ball.paddle_collide(paddle_group)
        my_ball.brick_collide(bricks_group)
        main_surface.blit(my_paddle.image, my_paddle.rect)
        my_ball.move()
        if my_ball.rect.bottom > application_height:
            num_turns -= 1
            my_ball.rect.x = 200
            my_ball.rect.y = 300
            main_surface.blit(my_ball.image, my_ball.rect)
        if num_turns == 0:
            main_surface.fill(white)
            myFont = pygame.font.SysFont("Times New Roman", 65)
            label = myFont.render("GAME OVER", 1, white)
            main_surface.blit(label, (200, 275))
            pygame.display.update()
            pygame.time.wait(100)
            break
        main_surface.blit(my_ball.image, my_ball.rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()


main()
