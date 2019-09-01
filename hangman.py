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

class Game:
    def __init__(self):
        # set title for the game window
        pygame.display.set_caption("Hangman")

        # clock that sets the amount of frames per second
        self.fps_clock = pygame.time.Clock()

        self.settings = Settings()

        # create display surface on which everithing is drawn
        self.DISPLAY_SURFACE = pygame.display.set_mode((self.settings.WINDOW_WIDTH, 
                                                    self.settings.WINDOW_HEIGHT))

        # create instance of figure class
        self.figure = Figure(self.DISPLAY_SURFACE)
        self.ta = TextArea(self.DISPLAY_SURFACE)

    def run(self):
        while True:
            self.DISPLAY_SURFACE.fill(self.settings.BLACK)

            # check key and mouse events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and self.ta.state == "active":
                    if 97 <= event.key <= 122:
                        self.ta.check_letter(chr(event.key))
                        self.ta.check_game_state()
                        self.figure.guesses = len(self.ta.guessed_wrong)
                elif event.type == KEYDOWN and self.ta.state != "active":
                    if event.key == K_RETURN or event.key == K_SPACE:
                        self.ta.reset_text()
                        self.figure.reset_figure()

            if self.ta.state == "active":
                self.ta.display_textarea()
            elif self.ta.state == "win":
                self.ta.display_win()
            elif self.ta.state == "lost":
                self.ta.display_lost()

            self.figure.draw_figure()
            
            pygame.display.update()
            self.fps_clock.tick(self.settings.FPS)
    
def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
