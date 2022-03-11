from game_state import GameState
from player import Player


N_TURNS = 6
WORD_LEN = 5


def main():
    game = GameState(N_TURNS, WORD_LEN)
    player = Player()
    correct_word = game.correct_word

    for _ in range(N_TURNS):
        word = player.choose_word(correct_word)
        letters = game.update(word)

        player.print_state(letters)

        if game.win:
            print('\n\nVOCE GANHOU')
            print('numero de rounds: ' + str(game.turns_played))
            break
        elif game.lose:
            print('\n\nVOCE PERDEU')
            print('palavra correta: ' + game.correct_word)


if __name__ == '__main__':
    main()