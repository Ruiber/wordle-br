from random import choice

from utils import translate

class WordSelector:
    def __init__(self, word_len):
        self.word_length = word_len
        
        with open(f'words/palavras_{word_len}', 'r') as file:
            self.words = [word.strip() for word in file]

        with open(f'words/palavras_possiveis_{word_len}', 'r') as file:
            self.valid_words = [translate(word.strip()) for word in file]
    
    
    def select_word(self):
        return choice(self.words)

    
    def is_valid_word(self, word):
        return word in self.valid_words
