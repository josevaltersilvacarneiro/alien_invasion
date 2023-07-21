import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class representing a single alien in the fleet.

    Attributes:
        screen (pygame.Surface): The game screen on which the alien will be displayed.
        ai_settings (Settings): An object containing the game settings.
        image (pygame.Surface): The image of the alien.
        rect (pygame.Rect): The rectangle representing the alien's position on the screen.
        x (float): The exact horizontal position of the alien.

    Methods:
        __init__(self, ai_settings, screen):
            Initializes an alien object and sets its initial position.

        blitme(self):
            Draws the alien at its current position.

        check_edges(self):
            Returns True if the alien is at the edge of the screen.

        update(self):
            Moves the alien to the right.

    """

    def __init__(self, ai_settings, screen):
        """Initializes an alien object and sets its initial position.

        Args:
            ai_settings (Settings): An object containing the game settings.
            screen (pygame.Surface): The game screen on which the alien will be displayed.

        """

        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('assets/images/alien.png')     # err
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the exact position of the alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Draws the alien at its current position on the screen.

        """

        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Returns True if the alien is at the edge of the screen.

        """

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Moves the alien to the right.

        """
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x
