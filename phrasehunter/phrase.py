from phrasehunter.constants import PHRASES


class Phrase:
    '''A class used to represent the phrase that a user will try to guess.

    Attributes
    ----------
        phrase : str
            The phrase passed through the constructor of the class.
        letters : set
            The unique letters derived from the phrase.
    '''
    phrase = None
    letters = None

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.letters_in_phrase = set(self.phrase)
        self.letters_in_phrase.discard(' ')

    def __eq__(self, other):
        return self.phrase == other

    def display(self, guessed_letters):
        '''Render the current phrase with guessed letters visible.
                Unguessed letters are rendered as underscores.
        '''
        output = []
        for letter in self.phrase:
            char = letter if letter == ' ' or letter in guessed_letters else '_'
            output.append(char)

        print(f"\n{' '.join(output)}\n")

    def check_letter(self, letter):
        '''Check if a letter is in the phrase.

        Parameters
        ----------
            letter : str
                The letter to check.

        Returns
        -------
            boolean
                True if letter is in the phrase, False otherwise.
        '''
        return letter in self.phrase

    def check_complete(self, guessed_letters):
        '''Check the difference of the unique letters in the phrase against a set of guessed letters.
                If the difference is an empty set then the phrase is completed.

        Parameters
        ----------
            guessed_letters : list
                A list of letters to check against the set of unique letters in the phrase.

        Returns
        -------
            boolean
                True if the difference is an empty set, False otherwise.
        '''
        return len(self.letters_in_phrase - set(guessed_letters)) == 0
