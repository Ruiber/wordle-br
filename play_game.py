from colorama import Fore
from string import ascii_lowercase

from game_state import GameState
from letter_state import LetterState

N_TURNS = 6
WORD_LEN = 5

def main():
    game = GameState(N_TURNS, WORD_LEN)

    for turn in range(N_TURNS):
        word = input('\nDigite sua palavra: ')
        game.update(word)
        print_state(game)

        if game.win:
            print('\n\nVOCE GANHOU')
            print('numero de rounds: ' + str(game.turns_played))
            break
        elif game.lose:
            print('\n\nVOCE PERDEU')
            print('palavra correta: ' + game.correct_word)


def print_state(game):
    state_to_color = {LetterState.NOT_USED: Fore.WHITE,
                    LetterState.NOT_IN_WORD: Fore.RED,
                    LetterState.WRONG_PLACE: Fore.YELLOW,
                    LetterState.RIGHT_PLACE: Fore.GREEN}

    for word in game.words_played:
        for i, letter in enumerate(word.guess):
            print(state_to_color[word.letter_states[i]] + letter, end=' ')
        print(Fore.WHITE)

    print()
    print()

    for letter in ascii_lowercase:
        print(state_to_color[game.letters[letter]] + letter, end=' ')
    print(Fore.WHITE)


if __name__ == '__main__':
    main()
