from string import ascii_lowercase

from word_selector import WordSelector
from letter_state import LetterState
from turn_state import TurnState
from utils import translate

# TODO: aumentar as palavras possiveis de serem chutadas, olhando para o dataset maior
class GameState:
    def __init__(self, n_turns, word_len):
        self.n_turns = n_turns
        self.word_len = word_len
        self.win = False
        self.lose = False
        self.turns_played = 0

        selector = WordSelector(word_len)
        self.correct_word = selector.select_word()
        self.compared_word = translate(self.correct_word)

        self.words_played = []
        self.possible_words = set(selector.words)
        self.letters = {letter: LetterState.NOT_USED for letter in ascii_lowercase}


    def update(self, new_word):
        self.words_played.append(TurnState(self.correct_word, new_word))
        self.update_letters(new_word)
        
        self.turns_played += 1
        if new_word == self.compared_word:
            self.win = True
        elif self.turns_played == self.n_turns:
            self.lose = True


    def update_letters(self, word):
        state = self.compare_words(word)

        for letter in state.keys():
            self.letters[letter] = max(self.letters[letter], state[letter])


    def compare_words(self, word):
        state = {letter: LetterState.NOT_IN_WORD for letter in word}
        unmatched_correct = []
        unmatched_new     = []

        for letter_correct, letter_new in zip(self.compared_word, word):
            if letter_new == letter_correct:
                state[letter_new] = LetterState.RIGHT_PLACE
            else:
                unmatched_correct.append(letter_correct)
                unmatched_new.append(letter_new)

        while len(unmatched_new) > 0:
            letter = unmatched_new.pop()
            if letter in unmatched_correct:
                unmatched_correct.remove(letter)
                state[letter] = max(state[letter], LetterState.WRONG_PLACE)

        return state
