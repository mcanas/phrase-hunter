from phrasehunter.constants import PHRASES


class Phrase:
    phrase = None
    letters = None

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.letters_in_phrase = set(self.phrase)
        self.letters_in_phrase.discard(' ')

    def __eq__(self, other):
        return self.phrase == other

    def display(self, guessed_letters):
        output = []
        for letter in self.phrase:
            char = letter if letter == ' ' or letter in guessed_letters else '_'
            output.append(char)

        print(f"\n{' '.join(output)}\n")

    def check_letter(self, letter):
        return letter in self.phrase

    def check_complete(self, guessed_letters):
        return len(self.letters_in_phrase - set(guessed_letters)) == 0
