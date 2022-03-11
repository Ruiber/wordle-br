from letter_state import LetterState

class TurnState:
    def __init__(self, correct, guess):
        self.guess = guess
        self.letter_states = [LetterState.NOT_IN_WORD for _ in range(len(correct))]

        already_used = {pos: False for pos in range(len(correct))}

        # Primeiro checo todos os corretos
        for i in range(len(guess)):
            if guess[i] == correct[i]:
                self.letter_states[i] = LetterState.RIGHT_PLACE
                already_used[i] = True

        for i in range(len(guess)):
            if guess[i] != correct[i]:
                for j in range(len(correct)):
                    if guess[i] == correct[j]:
                        if not already_used[j]:
                            self.letter_states[i] = LetterState.WRONG_PLACE
                            already_used[j] = True
                            break

