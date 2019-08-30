import pygame, random
from Settings import Settings

class TextArea(Settings):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.word = random.choice(self.WORD_LIST)
        self.word_display = "_" * len(self.word)
        self.guessed_correct = []
        self.guessed_wrong = []

    def check_letter(self, letter):
        if letter in self.word and letter not in self.guessed_correct:
            self.guessed_correct.append(letter)
        elif letter not in self.word and letter not in self.guessed_wrong:
            self.guessed_wrong.append(letter)

    def display_textarea(self):
        self.display_message()
        self.display_word()
        self.display_wrong_letters()

    def display_word(self):
        self.update_word()
        font = pygame.font.SysFont(None, 64)
        text = font.render(self.word_display, True, self.WHITE)
        
        self.screen.blit(text, (400, 300))

    def update_word(self):
        self.word_display = "".join(letter if letter in self.guessed_correct
                else "_" for letter in self.word)

    def display_wrong_letters(self):
        font = pygame.font.SysFont(None, 36)
        text = font.render("Guessed wrong: " 
                    + ", ".join(self.guessed_wrong), True, self.WHITE)
        
        self.screen.blit(text, (350, 400))

    def display_message(self):
        font = pygame.font.SysFont(None, 32)
        text = font.render("Press letter on keyboard to guess", True, self.WHITE)
        
        self.screen.blit(text, (350, 150))
        
