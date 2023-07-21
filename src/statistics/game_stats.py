class GameStats:
    """A class to store statistical data for the Alien Invasion game.

    Attributes:
        ai_settings (Settings): An object containing the game settings.
        ships_left (int): The number of remaining ships.
        score (int): The player's current score.
        level (int): The current game level.
        game_active (bool): A flag indicating whether the game is active (True) or inactive (False).
        high_score (int): The highest score achieved in the game.

    Methods:
        __init__(self, ai_settings):
            Initializes the statistical data.

        reset_stats(self):
            Initializes the statistical data that can change during the game.

    """

    def __init__(self, ai_settings):
        """Initializes the statistical data.

        Args:
            ai_settings (Settings): An object containing the game settings.

        """

        self.ai_settings = ai_settings
        self.reset_stats()

        # start the Alien Invasion game in an inactive state
        self.game_active = False

        # the high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initializes the statistical data that can change during the game.

        """

        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
