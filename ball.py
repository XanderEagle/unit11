import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, window_width, window_height, radius):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = color
        self.window_width = window_width
        self.window_height = window_height
        self.radius = radius

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.

        self.image = pygame.Surface((self.radius, self.radius))
        self.rect = self.image.get_rect()
        self.x_speed = 4
        self.y_speed = 5

        pygame.mixer.init(44100, -16, 2, 2048)
        self.sound = pygame.mixer.Sound("Lightsaber Turn On-SoundBible.com-647586083.wav")
        self.sound2 = pygame.mixer.Sound("Click2-Sebastian-759472264.wav")

        # Add a circle to represent the ball to the surface just created.

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.left < 0 or self.rect.right > self.window_width:
            self.x_speed = -self.x_speed
        if self.rect.top < 0 or self.rect.bottom > self.window_height:
            self.y_speed = -self.y_speed

    def paddle_collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.y_speed = -self.y_speed
            self.sound.play()

    def brick_collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.y_speed = -self.y_speed
            self.sound2.play()


