import pygame, os
from pygame.locals import *

from mario_mode.gamelib import menu
from mario_mode.gamelib import data

# Main function
def mario_mode_lunch():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mouse.set_visible(0)
    pygame.display.set_icon(pygame.image.load(data.filepath("icon.ico")))
    pygame.display.set_caption("mario mode")
    screen = pygame.display.set_mode((640, 480))
    menu.Menu(screen)
