import pygame
from Settings import Settings
class Figure(Settings):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.word = "python"
        self.x = 200
        self.y = 200
        self.state = "active"
        self.guesses = 6
    

    def draw_figure(self):
        if self.guesses >= 0:
            self.draw_gallows(self.screen)
        if self.guesses >= 1:
            self.draw_head(self.screen)
        if self.guesses >= 2:
            self.draw_body(self.screen)
        if self.guesses >= 3:
            self.draw_left_hand(self.screen)
        if self.guesses >= 4:
            self.draw_right_hand(self.screen)
        if self.guesses >= 5:
            self.draw_left_leg(self.screen)
        if self.guesses <= 6:
            self.draw_right_leg(self.screen)

    def draw_gallows(self, screen):
        pygame.draw.line(screen, self.WHITE, (130, 80), (250, 80), 3)
        pygame.draw.line(screen, self.WHITE, (250, 80), (250, 120), 3)
        pygame.draw.line(screen, self.WHITE, (130, 80), (130, 400), 3)
        pygame.draw.line(screen, self.WHITE, (60, 400), (200, 400), 3)

    def draw_head(self, screen):
        pygame.draw.circle(screen, self.WHITE, (250, 150), 30, 3)
    
    def draw_body(self, screen):
        pygame.draw.line(screen, self.WHITE, (250, 180), (250, 280), 3)

    def draw_left_hand(self, screen):
        pygame.draw.line(screen, self.WHITE, (250, 200), (210, 230), 3)

    def draw_right_hand(self, screen):
        pygame.draw.line(screen, self.WHITE, (250, 200), (290, 230), 3)

    def draw_left_leg(self, screen):
        pygame.draw.line(screen, self.WHITE, (250, 280), (200, 330), 3)

    def draw_right_leg(self, screen):
        pygame.draw.line(screen, self.WHITE, (250, 280), (300, 330), 3)