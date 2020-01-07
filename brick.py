import pygame

class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.width = width
        self.height = height
        self.color = color

        # Create a surface with the correct height and width
        self.image =

        # Get the rect coordinates
        self.rect =

        # Fill the surface with the correct color