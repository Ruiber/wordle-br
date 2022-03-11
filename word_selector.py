from random import choice

class WordSelector:
    def __init__(self, word_len):
        self.word_length = word_len
        
        with open(f'words/palavras_{word_len}', 'r') as file:
            self.words = [word.strip() for word in file]
    
    def select_word(self):
        return choice(self.words)
