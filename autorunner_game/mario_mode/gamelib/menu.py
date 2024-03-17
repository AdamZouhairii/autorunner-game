import pygame, sys
from pygame.locals import *
from mario_mode.gamelib.game import *
from mario_mode.gamelib.ezmenu import *
from mario_mode.gamelib.data import *
from mario_mode.gamelib.cutscenes import cutscene

def RunGame(screen):
    Game(screen)
    play_music("title.ogg", 0.75)
    
def ContinueGame(screen):
    Game(screen, True)
    play_music("title.ogg", 0.75)
               
def Help(screen):
    cutscene(screen, ["HELP",
    "",
    "Jump: Arrow key up",
    "Super Jump: Arrow keys up/right",
    "Return: Esc =return (last Esc = exit game not return to menu)",
    "Note: Jump on enemies to kill them!",
    ""])
    
class Menu(object):    

    def __init__(self, screen):
        self.screen = screen
        self.menu = EzMenu(["NEW GAME", lambda: RunGame(screen)], ["CONTINUE", lambda: ContinueGame(screen)], ["HELP", lambda: Help(screen)], ["QUIT GAME", sys.exit])
        self.menu.set_highlight_color((255, 0, 0))
        self.menu.set_normal_color((255, 255, 255))
        self.menu.center_at(300, 400)
        self.menu.set_font(pygame.font.Font(filepath("fonts/font.ttf"), 16))
        self.bg = load_image("menu.png")
        self.font = pygame.font.Font(filepath("fonts/font.ttf"), 16)
        self.font2 = pygame.font.Font(filepath("fonts/super-mario-64.ttf"), 45)
        play_music("title.ogg", 0.75)
        self.clock = pygame.time.Clock()
        events = pygame.event.get()
        self.menu.update(events)
        self.menu.draw(self.screen)
        self.main_loop()
  
    def main_loop(self):
        while 1:
            self.clock.tick(40)
            events = pygame.event.get()
            self.menu.update(events)
            for e in events:
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit()
                    return
                
            self.screen.blit(self.bg, (0, 0))
            ren = self.font.render("ready ???", 1, (255, 255, 255))
            self.screen.blit(ren, (320-ren.get_width()/2, 70))

            ren = self.font2.render("Mario Mode", 1, (255, 255, 255))
            self.screen.blit(ren, (320-ren.get_width()/2, 180))

            ren = self.font2.render("by the goat", 1, (255, 255, 255))
            self.screen.blit(ren, (320-ren.get_width()/2, 235))

            
            
            self.menu.draw(self.screen)
            pygame.display.flip()
