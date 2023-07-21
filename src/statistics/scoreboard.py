import pygame.font
from pygame.sprite import Group

from src.characters.ship import Ship


class Scoreboard:
    """A class to display scoring information.

    Attributes:
        screen (pygame.Surface): The game screen on which the scoring information will be displayed.
        screen_rect (pygame.Rect): The rectangle representing the dimensions of the game screen.
        ai_settings (Settings): An object containing the game settings.
        stats (GameStats): An object containing the game statistical data.
        text_color (tuple): The RGB color tuple representing the color of the text.
        font (pygame.font.Font): The font used for rendering the text.
        score_image (pygame.Surface): The rendered image of the current score.
        score_rect (pygame.Rect): The rectangle representing the position of the score image on the screen.
        high_score_image (pygame.Surface): The rendered image of the high score.
        high_score_rect (pygame.Rect): The rectangle representing the position of the high score image on the screen.
        level_image (pygame.Surface): The rendered image of the current game level.
        level_rect (pygame.Rect): The rectangle representing the position of the level image on the screen.
        ships (Group): A group of spaceship instances representing the remaining ships.

    Methods:
        __init__(self, ai_settings, screen, stats):
            Initializes the attributes of the scoreboard.

        prep_score(self):
            Converts the score into a rendered image.

        prep_high_score(self):
            Converts the high score into a rendered image.

        show_score(self):
            Draws the score, high score, level, and remaining ships on the screen.

        prep_level(self):
            Converts the level into a rendered image.

        prep_ships(self):
            Displays the remaining ships on the screen.

    """

    def __init__(self, ai_settings, screen, stats):
        """Initializes the attributes of the scoreboard.

        Args:
            ai_settings (Settings): An object containing the game settings.
            screen (pygame.Surface): The game screen on which the scoring information will be displayed.
            stats (GameStats): An object containing the game statistical data.

        """

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Converts the score into a rendered image.

        """

        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # display the score at the top-right in corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Converts the high score into a rendered image.

        """

        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)

        # center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draws the score, high score, level, and remaining ships on the screen.

        """

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # draw the remaining ships
        self.ships.draw(self.screen)

    def prep_level(self):
        """Converts the level into a rendered image.

        """

        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.ai_settings.bg_color)

        # position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Displays the remaining ships on the screen.

        """

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
