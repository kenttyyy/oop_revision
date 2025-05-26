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

    def save_to_file(self, filename="quiz_questions.txt"):
        with open(filename, "a") as file:
            file.write(f"Question: {self.text}\n")
            for key, value in self.choices.items():
                file.write(f"{key}. {value}\n")
            file.write(f"Correct Answer: {self.correct_answer}\n\n")

class QuizCreator:
    def __init__(self):
        self.colors = AnsiColor()

    # [4] move menu and user input logic into QuizCreator methods
    def display_menu(self):
        print(f"{self.colors.BOLD}{self.colors.CYAN}What do you want to do?")
        print(f"{self.colors.YELLOW}Type 1 - Add A Question")
        print(f"{self.colors.YELLOW}Type 2 - Exit")

    def get_user_choice(self):
        try:
            return int(input(f"{self.colors.MAGENTA}Enter your choice 1 or 2: "))
        except ValueError:
            return -1