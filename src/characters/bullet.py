import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class that manages projectiles fired by the spaceship.

    Attributes:
        screen (pygame.Surface): The game screen on which the bullet will be displayed.
        rect (pygame.Rect): The rectangle representing the bullet's position on the screen.
        y (float): The vertical position of the bullet.
        color (tuple): The color of the bullet.
        speed_factor (float): The speed factor at which the bullet moves.

    Methods:
        __init__(self, ai_settings, screen, ship):
            Creates a bullet object at the current position of the spaceship.

        update(self):
            Moves the bullet upward on the screen.

        draw_bullet(self):
            Draws the bullet on the screen.

    """

    def __init__(self, ai_settings, screen, ship):
        """Creates a bullet object at the current position of the spaceship.

        Args:
            ai_settings (Settings): An object containing the game settings.
            screen (pygame.Surface): The game screen on which the bullet will be displayed.
            ship (Ship): The spaceship object from which the bullet is fired.

        """

        super(Bullet, self).__init__()  # testar super().__init__()
        self.screen = screen

        # create a rectangle for the bullet at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the position of the bullet as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves the bullet upward on the screen.

        """

        # update the decimal position of the bullet
        self.y -= self.speed_factor

        # update the position of rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet on the screen.

        """

        pygame.draw.rect(self.screen, self.color, self.rect)
