import pygame.font


class Button:
    """A class representing a button on the screen.

    Attributes:
        screen (pygame.Surface): The game screen on which the button will be displayed.
        screen_rect (pygame.Rect): The rectangle representing the dimensions of the game screen.
        width (int): The width of the button.
        height (int): The height of the button.
        button_color (tuple): The RGB color tuple representing the button's background color.
        text_color (tuple): The RGB color tuple representing the button's text color.
        font (pygame.font.Font): The font used for rendering the button's text.
        rect (pygame.Rect): The rectangle representing the button's position and size on the screen.
        msg_image (pygame.Surface): The rendered text image of the button's message.
        msg_image_rect (pygame.Rect): The rectangle representing the position of the button's message on the screen.

    Methods:
        __init__(self, ai_settings, screen, msg):
            Initializes the attributes of the button.

        prep_msg(self, msg):
            Converts the message into a rendered image and centers the text on the button.

        draw_button(self):
            Draws a blank button on the screen and then draws the button's message.

    """

    def __init__(self, ai_settings, screen, msg):
        """Initializes the attributes of the button.

        Args:
            ai_settings (Settings): An object containing the game settings.
            screen (pygame.Surface): The game screen on which the button will be displayed.
            msg (str): The message to be displayed on the button.

        """

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # define the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)     # green color for the button
        self.text_color = (255, 255, 255)   # white color for the button text
        self.font = pygame.font.SysFont(None, 48)   # use the default system font with a size of 48

        # construct the rect object for the button and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the button's message needs to be prepared only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Converts the message into a rendered image and centers the text on the button.

        Args:
            msg (str): The message to be displayed on the button.

        """

        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draws a blank button on the screen and then draws the button's message.

        """

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
