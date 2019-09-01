# hangman game
# guess the hidden word before you run out of tries
# author: Nick Poberezhnyk
# nick.poberezhnyk@gmail.com

import sys, pygame
from pygame.locals import *
from Settings import Settings
from Figure import Figure
from TextArea import TextArea
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
ta = TextArea(DISPLAY_SURFACE)

while True:
    DISPLAY_SURFACE.fill(settings.BLACK)

    # check key and mouse events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and ta.state == "active":
            if 97 <= event.key <= 122:
                ta.check_letter(chr(event.key))
                ta.check_game_state()
                figure.guesses = len(ta.guessed_wrong)
        elif event.type == KEYDOWN and ta.state != "active":
            if event.key == K_RETURN or event.key == K_SPACE:
                ta.reset_text()
                figure.reset_figure()

    if ta.state == "active":
        ta.display_textarea()
    elif ta.state == "win":
        ta.display_win()
    elif ta.state == "lost":
        ta.display_lost()

    figure.draw_figure()
    
    pygame.display.update()
    fps_clock.tick(settings.FPS)
    