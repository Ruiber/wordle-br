def translate(word):
    letter_change = {'ç': 'c', 'Ç': 'C',
                    'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A',
                    'é': 'e', 'ê': 'e', 'É': 'E', 'Ê': 'E',
                    'í': 'i', 'Í': 'I',
                    'ó': 'o', 'ô': 'o', 'õ': 'o', 'Ó': 'O', 'Ô': 'O', 'Õ': 'O',
                    'ú': 'u', 'ü': 'u', 'Ú': 'U', 'Ü': 'U'}
    out = ''
    if type(word) is str:
        for ch in word:
            if ch in letter_change.keys():
                out += letter_change[ch]
            else:
                out += ch
            
    return out