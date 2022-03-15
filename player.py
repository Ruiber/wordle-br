from colorama import Fore
from string import ascii_lowercase

from letter_state import LetterState
from turn_state import TurnState
from word_selector import WordSelector

class Player:
    def __init__(self, word_len):
        self.words_played = []
        self.word_len = word_len
        self.word_selector = WordSelector(word_len)


    def print_state(self, letters):
        state_to_color = {LetterState.NOT_USED: Fore.WHITE,
                        LetterState.NOT_IN_WORD: Fore.RED,
                        LetterState.WRONG_PLACE: Fore.YELLOW,
                        LetterState.RIGHT_PLACE: Fore.GREEN}

        for word in self.words_played:
            for i, letter in enumerate(word.guess):
                print(state_to_color[word.letter_states[i]] + letter, end=' ')
            print(Fore.WHITE)

        print()
        print()

        for letter in ascii_lowercase:
            print(state_to_color[letters[letter]] + letter, end=' ')
        print(Fore.WHITE)

    
    def choose_word(self, correct_word):
        word = input('\nDigite sua palavra: ')

        if not self.is_valid(word):
            print('\nEntrada inválida. Tente novamente\n')
            return self.choose_word(correct_word)

        self.words_played.append(TurnState(correct_word, word))
        return word

    
    def is_valid(self, word):
        return len(word) == self.word_len and self.word_selector.is_valid_word(word)
