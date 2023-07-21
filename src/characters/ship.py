import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class representing the player's spaceship.

    Attributes:
        screen (pygame.Surface): The game screen on which the spaceship will be displayed.
        ai_settings (Settings): An object containing the game settings.
        image (pygame.Surface): The image of the spaceship.
        rect (pygame.Rect): The rectangle representing the spaceship's position on the screen.
        screen_rect (pygame.Rect): The rectangle representing the dimensions of the game screen.
        center (float): The horizontal position of the spaceship's center.
        moving_right (bool): A flag indicating whether the spaceship is moving right.
        moving_left (bool): A flag indicating whether the spaceship is moving left.

    Methods:
        __init__(self, ai_settings, screen):
            Initializes the spaceship and sets its initial position.

        update(self):
            Updates the spaceship's position based on the movement flags.

        blitme(self):
            Draws the spaceship at its current position on the screen.

        center_ship(self):
            Centers the spaceship on the screen horizontally.

    """

    def __init__(self, ai_settings, screen):
        """Initializes the spaceship and sets its initial position.

        Args:
            ai_settings (Settings): An object containing the game settings.
            screen (pygame.Surface): The game screen on which the spaceship will be displayed.

        """

        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the spaceship image and set its rect attribute
        self.image = pygame.image.load('assets/images/ship.png')  # spaceship image
        self.rect = self.image.get_rect()   # a rectangle being created from the image's dimensions
        self.screen_rect = screen.get_rect()  # the rectangle is being placed on the screen

        # start each new spaceship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the center of the spaceship
        self.center = float(self.rect.centerx)

        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the spaceship's position based on the movement flags.

        """

        # update the value of the spaceship's center, not the rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update the rect object based on self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draws the spaceship at its current position on the screen.

        """

        self.screen.blit(self.image, self.rect)  # COINCIDINDO O RETÂNGULO COM A ESPAÇONAVE (OU RETÂNGULO DA ESPAÇONAVE)

    def center_ship(self):
        """Centers the spaceship on the screen horizontally.

        """

        self.center = self.screen_rect.centerx
