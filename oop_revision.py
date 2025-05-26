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

    def create_question(self):
        question_text = input(f"{self.colors.BOLD}{self.colors.GREEN}Enter a question: ")
        choice_a = input(f"{self.colors.CYAN}Enter Choice A: ")
        choice_b = input(f"{self.colors.CYAN}Enter Choice B: ")
        choice_c = input(f"{self.colors.CYAN}Enter Choice C: ")
        choice_d = input(f"{self.colors.CYAN}Enter Choice D: ")
        correct = input(f"{self.colors.CYAN}Enter the correct answer: ")

        question = Question(question_text, choice_a, choice_b, choice_c, choice_d, correct)
        question.save_to_file()

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == 1:
                self.create_question()
            elif choice == 2:
                print(f"{self.colors.BOLD}{self.colors.MAGENTA}Exiting the Quiz Creator.")
                break
            else:
                print(f"{self.colors.RED}Invalid input. Please enter 1 or 2.")

# [6] finalize main program with run logic and file writing
if __name__ == "__main__":
    quiz_creator = QuizCreator()
    quiz_creator.run()

# Program 10

class AnsiColor:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

class Question:
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer.upper()

    def ask(self, number, colors):
        print(f"\n{colors.BOLD}{colors.CYAN}Question {number}: {self.text}")
        for key, value in self.choices.items():
            print(f"{key}. {value}")
        user_answer = input(f"{colors.MAGENTA}Your answer (A/B/C/D): ").strip().upper()
        return user_answer == self.correct_answer, self.correct_answer

class QuizLoader:
    def __init__(self, filename):
        self.filename = filename

    def load_questions(self):
        with open(self.filename, "r") as file:
            lines = [line.strip() for line in file if line.strip() != ""]

        questions = []
        i = 0
        while i < len(lines):
            if lines[i].startswith("Question:"):
                text = lines[i][len("Question: "):]
                choices = {
                    "A": lines[i+1][len("A. "):],
                    "B": lines[i+2][len("B. "):],
                    "C": lines[i+3][len("C. "):],
                    "D": lines[i+4][len("D. "):],
                }
                correct = lines[i+5][len("Correct Answer: "):]
                questions.append(Question(text, choices, correct))
                i += 6
            else:
                i += 1
        return questions

class QuizRunner:
    def __init__(self, questions):
        self.questions = questions
        self.colors = AnsiColor()
        self.score = 0

    def run(self):
        if not self.questions:
            print(f"{self.colors.RED}No questions found. Please add questions using the Quiz Creator.")
            return

        random.shuffle(self.questions)

        for i, question in enumerate(self.questions, 1):
            correct, correct_answer = question.ask(i, self.colors)
            if correct:
                print(f"{self.colors.GREEN}Correct!")
                self.score += 1
            else:
                print(f"{self.colors.RED}Incorrect! The correct answer was {correct_answer}.")

        print(f"\n{self.colors.BOLD}{self.colors.YELLOW}Quiz completed! Your score: {self.score}/{len(self.questions)}{self.colors.RESET}")

if __name__ == "__main__":
    loader = QuizLoader("quiz_questions.txt")
    questions = loader.load_questions()
    quiz = QuizRunner(questions)
    quiz.run()