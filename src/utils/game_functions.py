import sys
from time import sleep

import pygame

from src.characters.bullet import Bullet
from src.characters.alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responds to key presses.

    """

    if event.key == pygame.K_RIGHT:     # right key is pressed
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:    # left key is pressed
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # creates a new bullet and adds it to the group of bullets
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:       # end the game
        sys.exit()


def check_keyup_events(event, ship):
    """Responds to key releases.

    """

    if event.key == pygame.K_RIGHT:     # right key is released
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:    # left key is released
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Responds to key presses and mouse events.

    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # end the game
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # some key is pressed
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:    # no key is pressed
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                      aliens, bullets, mouse_x, mouse_y):
    """Starts a new game when the player clicks 'Play'.

    """

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        # resets the game settings
        ai_settings.initialize_dynamic_settings()

        # hides the mouse cursor
        pygame.mouse.set_visible(False)

        # resets the game statistical data
        stats.reset_stats()
        stats.game_active = True

        # resets the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # empties the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # creates a new fleet and centers the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Updates images on the screen and flips to the new screen.

    """

    # redraws the screen on each pass through the loop
    screen.fill(ai_settings.bg_color)

    # redraws all bullets behind the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # draws the scoring information
    sb.show_score()

    # draws the Play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # makes the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Updates the position of bullets and gets rid of old bullets.

    """

    # updates the position of bullets
    bullets.update()

    # gets rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_high_score(stats, sb):
    """Checks if there's a new high score.

    """

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets):
    """Responds to collisions between bullets and aliens.

    """

    # removes any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # destroys existing bullets and creates a new fleet
        bullets.empty()
        ai_settings.increase_speed()

        # increases the level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fires a bullet if the limit has not been reached yet.

    """

    # creates a new bullet and adds it to the group of bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens(ai_settings, alien_width):
    """
    DETERMINA O NÚMERO DE ALIENÍGENAS QUE CABEM EM CADA LINHA.
    """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determines the number of rows with aliens that can fit on the screen.

    Args:
        ai_settings (Settings): An object containing the game settings.
        ship_height (int): The height of the player's spaceship.
        alien_height (int): The height of an alien.

    Returns:
        int: The number of rows of aliens that can fit on the screen.

    """

    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creates an alien and places it in the row.

    Args:
        ai_settings (Settings): An object containing the game settings.
        screen (pygame.Surface): The game screen where the alien will be placed.
        aliens (pygame.sprite.Group): A group of alien instances.
        alien_number (int): The position of the alien in the row.
        row_number (int): The row number where the alien will be placed.

    """

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Creates a complete fleet of aliens.

    Args:
        ai_settings (Settings): An object containing the game settings.
        screen (pygame.Surface): The game screen where the fleet of aliens will be created.
        ship (Ship): The player's spaceship.
        aliens (pygame.sprite.Group): A group of alien instances.

    """

    # create an alien and calculate the number of aliens in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Responds appropriately if any alien reaches an edge.

    Args:
        ai_settings (Settings): An object containing the game settings.
        aliens (pygame.sprite.Group): A group of alien instances.

    """

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Makes the entire fleet move down and changes its direction.

    Args:
        ai_settings (Settings): An object containing the game settings.
        aliens (pygame.sprite.Group): A group of alien instances.

    """

    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responds to the player's spaceship being hit by an alien.

    Args:
        ai_settings (Settings): An object containing the game settings.
        screen (pygame.Surface): The game screen where the player's spaceship and aliens are displayed.
        stats (GameStats): An object containing the game statistical data.
        sb (Scoreboard): An object representing the scoreboard.
        ship (Ship): The player's spaceship.
        aliens (pygame.sprite.Group): A group of alien instances.
        bullets (pygame.sprite.Group): A group of bullet instances.

    """

    if stats.ships_left > 0:
        # decrement ships_left
        stats.ships_left -= 1

        # update the scoreboard
        sb.prep_ships()

        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet and center the spaceship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause briefly
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Checks if any alien has reached the bottom of the screen.

    Args:
        ai_settings (Settings): An object containing the game settings.
        screen (pygame.Surface): The game screen where the player's spaceship and aliens are displayed.
        stats (GameStats): An object containing the game statistical data.
        sb (Scoreboard): An object representing the scoreboard.
        ship (Ship): The player's spaceship.
        aliens (pygame.sprite.Group): A group of alien instances.
        bullets (pygame.sprite.Group): A group of bullet instances.

    """

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # handle the same case as when the spaceship is hit
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Checks if the fleet is at an edge and then updates the positions of all aliens
    in the fleet.

    Args:
        ai_settings (Settings): An object containing the game settings.
        screen (pygame.Surface): The game screen where the player's spaceship and aliens are displayed.
        stats (GameStats): An object containing the game statistical data.
        sb (Scoreboard): An object representing the scoreboard.
        ship (Ship): The player's spaceship.
        aliens (pygame.sprite.Group): A group of alien instances.
        bullets (pygame.sprite.Group): A group of bullet instances.

    """

    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check for collisions between aliens and the spaceship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # check if any alien has reached the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
