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
        self.state = "active"

    # reset textarea
    def reset_text(self):
        self.state = "active"
        self.word = random.choice(self.WORD_LIST)
        self.word_display = "_" * len(self.word)
        self.guessed_correct = []
        self.guessed_wrong = []

    # check current game state
    def check_game_state(self):
        if len(self.guessed_correct) == len(self.word):
            self.state = "win"
        elif len(self.guessed_wrong) == 6:
            self.state = "lost"

    # check wether letter is in word and append it to appropriate list
    def check_letter(self, letter):
        if letter in self.word and letter not in self.guessed_correct:
            self.guessed_correct.extend([letter] * self.word.count(letter))
        elif letter not in self.word and letter not in self.guessed_wrong:
            self.guessed_wrong.append(letter)

    # area while guessing a word
    def display_textarea(self):
        self.display_message()
        self.display_word()
        self.display_wrong_letters()

    # text at win state
    def display_win(self):
        self.display_win_lost("YOU WIN!", self.GREEN)
        self.display_word()
        self.display_play_again_msg("Press enter or space to play again!")

    # text at lost state
    def display_lost(self):
        self.display_win_lost("YOU LOST!", self.RED)
        self.display_word()
        self.display_play_again_msg("Press enter or space to try again!")

    # message at the end of the screen to play again
    def display_play_again_msg(self, msg):
        font = pygame.font.SysFont(None, 48)
        text = font.render(msg, True, self.WHITE)
        text_rect = text.get_rect()
        text_rect.center = ((self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 6 * 5))
        self.screen.blit(text, text_rect)

    # word while guessing
    def display_word(self):
        self.word_display = "".join(letter if letter in self.guessed_correct
                else "_" for letter in self.word)
        font = pygame.font.SysFont("consolas", 64)
        text = font.render(self.word_display, True, self.WHITE)
        text_rect = text.get_rect()
        text_rect.center = ((530, 300))
        self.screen.blit(text, text_rect)

    # helper function to render win or lost message
    def display_win_lost(self, msg, color):
        font = pygame.font.SysFont(None, 100)
        text = font.render(msg, True, color)
        text_rect = text.get_rect()
        text_rect.center = ((530, 200))
        self.screen.blit(text, text_rect)
    
    # wrong letters under the word area
    def display_wrong_letters(self):
        font = pygame.font.SysFont(None, 36)
        text = font.render("Guessed wrong: " 
                    + ", ".join(self.guessed_wrong), True, self.WHITE)
        self.screen.blit(text, (350, 400))

    # message above the guessed word
    def display_message(self):
        font = pygame.font.SysFont(None, 32)
        text = font.render("Press letter on keyboard to guess", True, self.WHITE)
        self.screen.blit(text, (350, 150))
        
