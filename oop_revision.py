# Program 9

class AnsiColor:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

class Question:
    def __init__(self, text, choice_a, choice_b, choice_c, choice_d, correct_answer):
        self.text = text
        self.choices = {
            "A": choice_a,
            "B": choice_b,
            "C": choice_c,
            "D": choice_d
        }
        self.correct_answer = correct_answer