from colorama import Fore
from string import ascii_lowercase

from letter_state import LetterState
from turn_state import TurnState

#TODO: transformar o player em uma classe e trazer a lista de palavras jogadas para o player
class Player:
    def __init__(self):
        self.words_played = []


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

    
    #TODO: checar validade da palavra
    def choose_word(self, correct_word):
        word = input('\nDigite sua palavra: ')
        self.words_played.append(TurnState(correct_word, word))
        return word
