import pygame
from Settings import Settings
class Figure(Settings):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.x = 200
        self.y = 200
        self.state = "active"
        self.guesses = 0
        self.hangman_color = self.WHITE

    def draw_figure(self):
        if self.guesses >= 0:
            self.draw_gallows()
        if self.guesses >= 1:
            self.draw_head()
        if self.guesses >= 2:
            self.draw_body()
        if self.guesses >= 3:
            self.draw_left_hand()
        if self.guesses >= 4:
            self.draw_right_hand()
        if self.guesses >= 5:
            self.draw_left_leg()
        if self.guesses >= 6:
            self.draw_right_leg()
            self.hangman_color = self.RED


    def draw_gallows(self):
        pygame.draw.line(self.screen, self.hangman_color, (130, 80), (250, 80), 3)
        pygame.draw.line(self.screen, self.hangman_color, (250, 80), (250, 120), 3)
        pygame.draw.line(self.screen, self.hangman_color, (130, 80), (130, 400), 3)
        pygame.draw.line(self.screen, self.hangman_color, (60, 400), (200, 400), 3)

    def draw_head(self):
        pygame.draw.circle(self.screen, self.hangman_color, (250, 150), 30, 3)
    
    def draw_body(self):
        pygame.draw.line(self.screen, self.hangman_color, (250, 180), (250, 280), 3)

    def draw_left_hand(self):
        pygame.draw.line(self.screen, self.hangman_color, (250, 200), (210, 230), 3)

    def draw_right_hand(self):
        pygame.draw.line(self.screen, self.hangman_color, (250, 200), (290, 230), 3)

    def draw_left_leg(self):
        pygame.draw.line(self.screen, self.hangman_color, (250, 280), (200, 330), 3)

    def draw_right_leg(self):
        pygame.draw.line(self.screen, self.hangman_color, (250, 280), (300, 330), 3)