import pygame

class EzMenu:
    """
    A class representing a menu in a Pygame application.

    Attributes:
        options (tuple): The menu options, each represented as a tuple of (text, callback) pairs.
        x (int): The x-coordinate of the menu's position.
        y (int): The y-coordinate of the menu's position.
        font (pygame.font.Font): The font used for rendering the menu text.
        option (int): The currently selected menu option.
        width (int): The width of the menu.
        color (list): The color of the menu text.
        hcolor (list): The highlight color of the selected menu option.
        height (int): The height of the menu.

    Methods:
        draw(surface): Draws the menu on the given surface.
        update(events): Updates the menu based on the given events.
        set_pos(x, y): Sets the position of the menu.
        set_font(font): Sets the font used for rendering the menu text.
        set_highlight_color(color): Sets the highlight color of the selected menu option.
        set_normal_color(color): Sets the color of the menu text.
        center_at(x, y): Centers the menu at the given position.
    """

    def __init__(self, *options):
        """
        Initializes a new instance of the EzMenu class.

        Args:
            *options: Variable number of menu options, each represented as a tuple of (text, callback) pairs.
        """
        self.options = options
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font(None, 32)
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [255, 0, 0]
        self.height = len(self.options)*self.font.get_height()
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, 1, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()

    def draw(self, surface):
        """
        Draws the menu on the given surface.

        Args:
            surface (pygame.Surface): The surface on which to draw the menu.
        """
        i=0
        for o in self.options:
            if i==self.option:
                clr = self.hcolor
            else:
                clr = self.color
            text = o[0]
            ren = self.font.render(text, 1, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, ((self.x+self.width/2) - ren.get_width()/2, self.y + i*(self.font.get_height()+4)))
            i+=1
            
    def update(self, events):
        """
        Updates the menu based on the given events.

        Args:
            events (list): A list of pygame events.
        """
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.option += 1
                if e.key == pygame.K_UP:
                    self.option -= 1
                if e.key == pygame.K_RETURN:
                    self.options[self.option][1]()
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1

    def set_pos(self, x, y):     
        """
        Sets the position of the menu.

        Args:
            x (int): The x-coordinate of the menu's position.
            y (int): The y-coordinate of the menu's position.
        """
        self.x = x
        self.y = y
        
    def set_font(self, font):
        """
        Sets the font used for rendering the menu text.

        Args:
            font (pygame.font.Font): The font used for rendering the menu text.
        """
        self.font = font
        
    def set_highlight_color(self, color):
        """
        Sets the highlight color of the selected menu option.

        Args:
            color (list): The highlight color of the selected menu option.
        """
        self.hcolor = color
        
    def set_normal_color(self, color):
        """
        Sets the color of the menu text.

        Args:
            color (list): The color of the menu text.
        """
        self.color = color
        
    def center_at(self, x, y):
        """
        Centers the menu at the given position.

        Args:
            x (int): The x-coordinate of the position to center the menu at.
            y (int): The y-coordinate of the position to center the menu at.
        """
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)
