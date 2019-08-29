# hangman game
# guess the hidden word before you run out of tries
# author: Nick Poberezhnyk

import sys, pygame
from pygame.locals import *
from Settings import Settings
from Figure import Figure
pygame.init()

# set title for the game window
pygame.display.set_caption("Hangman")

# clock that sets the amount of frames per second
fps_clock = pygame.time.Clock()

settings = Settings()

# create display surface on which everithing is drawn
DISPLAY_SURFACE = pygame.display.set_mode((settings.WINDOW_WIDTH, 
                                            settings.WINDOW_HEIGHT))

# create instance of figure class
figure = Figure(DISPLAY_SURFACE)

while True:
    DISPLAY_SURFACE.fill(settings.BLACK)

    # check key and mouse events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    figure.draw_figure()
    pygame.display.update()
    fps_clock.tick(settings.FPS)
    