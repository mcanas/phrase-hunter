import random
from phrasehunter.constants import PHRASES, WELCOME, VALID_CHARS, YOU_WIN, YOU_LOSE
from phrasehunter.phrase import Phrase


class Game:
    '''The Game class controls the flow of Phrase Hunter game

    Attributes
    ----------
        lives : int 
            The number of misses a player can make before the game is over. Defaults to 5.
        missed : int
            A running tally of missed guesses per game. Defaults to 0.
        phrases : Phrase[]
            Stores the history of phrases as Phrase instances used per game. Defaults to [].
        active_phrase : Phrase
            The current phrase as a Phrase instance. Defaults to None.
        guesses : str[]
            Stores a history of guessed letters. Defaults to [].
    '''

    def __init__(self):
        '''Sets the default values for the attributes of the Game class.
        '''
        self.lives = 5
        self.missed = 0
        self.phrases = []
        self.active_phrase = None
        self.guesses = []

    def start(self):
        '''Starts the game loop.
        '''
        self.welcome()

        while True:
            # Determine if the game has been started
            #   otherwise get game start confirmation
            if self.active_phrase is None:
                if self.confirm_game_start():
                    self.active_phrase = self.get_random_phrase()
                else:
                    print('\nGoodbye!')
                    break

            # Display progress and get a valid guess
            self.active_phrase.display(self.guesses)
            guess = self.get_guess()
            self.guesses.append(guess)

            # Check if the game has been won or lost
            if self.active_phrase.check_letter(guess):
                if self.active_phrase.check_complete(self.guesses):
                    self.game_over(True)
            else:
                self.missed += 1
                print(
                    f'\nYou have {self.lives - self.missed} out of {self.lives} lives remaining!')
                if self.missed == self.lives:
                    self.game_over(False)

    def welcome(self):
        '''Print a welcome message to the console.
        '''
        print(WELCOME)

    def confirm_game_start(self):
        '''Get confirmation for starting a new game.
        '''
        while True:
            confirm_game_start = input(
                'Would you like to start a new game? (Y/N) ').lower()

            try:
                if confirm_game_start not in ('y', 'n'):
                    raise ValueError('Invalid answer.')
            except ValueError as err:
                print(f'\nOops! Something went wrong: {err}\n')
            else:
                return True if confirm_game_start == 'y' else False

    def get_random_phrase(self):
        '''Get a random phrase from the phrase library and create
            a new Phrase object.
        '''
        while True:
            random_phrase = random.choice(PHRASES)
            if random_phrase not in self.phrases:
                self.phrases.append(Phrase(random_phrase))
                return self.phrases[-1]

    def get_guess(self):
        '''Get a single a-z letter from input.
        '''
        while True:
            guess = input('Enter a letter to make your next guess: ')
            guess = guess.lower()
            try:
                if guess not in VALID_CHARS:
                    raise ValueError(
                        'You entered an invalid character. Please try again.')
            except ValueError as err:
                print(f'\nOops! Something went wrong: {err}\n')
            else:
                return guess

    def game_over(self, is_win):
        '''Ends the current game and resets default values to prepare for the next game.

        Parameters
        ----------
        is_win : boolean
            A flag used to determine the win or lose message that will print to the console.
        '''
        self.active_phrase.display(self.guesses)
        print(f'\n{YOU_WIN if is_win else YOU_LOSE}\n')
        self.active_phrase = None
        self.guesses = []
        self.missed = 0
