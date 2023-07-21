class Settings:
    """A class to store all the game settings.

    Attributes:
        screen_width (int): The width of the game screen.
        screen_height (int): The height of the game screen.
        bg_color (tuple): The RGB color tuple representing the background color of the game screen.
        ship_limit (int): The number of ships the player has before the game ends.
        bullet_width (int): The width of the bullets fired by the spaceship.
        bullet_height (int): The height of the bullets fired by the spaceship.
        bullet_color (tuple): The RGB color tuple representing the color of the bullets.
        bullets_allowed (int): The maximum number of bullets allowed on the screen simultaneously.
        fleet_drop_speed (int): The speed at which the fleet of aliens moves downward.
        speedup_scale (float): The rate at which the game speed increases.
        score_scale (float): The rate at which the points for each alien increase.

    Methods:
        __init__(self):
            Initializes the game settings.

        initialize_dynamic_settings(self):
            Initializes the settings that change during the game.

        increase_speed(self):
            Increases the game speed settings and alien points.

    """

    def __init__(self):
        """Initializes the game settings.

        """

        # screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10

        # speedup settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes the settings that change during the game.

        """

        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction equal to 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increases the game speed settings and alien points.

        """

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
