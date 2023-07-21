import pygame
from pygame.sprite import Group

from src.gui.settings import Settings
from src.gui.button import Button

from src.statistics.game_stats import GameStats
from src.statistics.scoreboard import Scoreboard
from src.characters.ship import Ship

import src.utils.game_functions as gf


def main():
    """Initializes pygame, settings and the screen object.

    """

    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # creates the play button
    play_button = Button(ai_settings, screen, "Play")

    # creates an instance to store game statistics data
    # and creates scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # creates a spaceship, a group of projectiles and
    # a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # creates the fleet of aliengens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # starts the main game loop
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button,
                        ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            # get rid of projectiles and aliens that have
            # disappeared
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)


if __name__ == '__main__':
    main()
