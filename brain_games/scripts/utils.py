import random
from abc import ABC, abstractmethod

import prompt


class Game(ABC):
    def __init__(self):
        self.player_name = None
        self.questions_count = 3

    def start(self):
        self._greeting()
        self._get_player_name()

        if self._play_rounds():
            self._congratulate()
        else:
            self._loose_output()

    def _play_rounds(self):
        self._get_game_header()
        for round_num in range(self.questions_count):
            question_data = self._generate_question()
            print(f"Question: {question_data['question']}")

            user_answer = self._get_answer()

            if not self._check_answer(question_data, user_answer):
                print(
                    f"'{user_answer}' is wrong answer ;(. "
                    f"Correct answer was '{question_data['correct_answer']}'."
                )
                return False
            print("Correct!")
        return True

    @abstractmethod
    def _get_game_header(self):
        pass

    @abstractmethod
    def _generate_question(self):
        pass

    @abstractmethod
    def _check_answer(self, question_data, answer):
        pass

    def _greeting(self) -> None:
        print("Welcome to the Brain Games!")

    def _get_player_name(self):
        while self.player_name is None or len(self.player_name) == 0:
            self.player_name = prompt.string("May I have your name? ")
        print(f"Hello, {self.player_name}!")

    @staticmethod
    def _get_answer() -> str:
        return prompt.string("Your answer: ")

    def _congratulate(self) -> None:
        print(f"Congratulations, {self.player_name}!")

    def _loose_output(self) -> None:
        print(f"Try again, {self.player_name}")


class BrainGames(Game):
    def start(self):
        self._greeting()
        self._get_player_name()

    def _get_game_header(self):
        pass

    def _generate_question(self):
        pass

    def _check_answer(self, question_data, answer):
        pass


class GameBrainEven(Game):
    def _get_game_header(self):
        print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    def _generate_question(self) -> dict:
        number = random.randint(0, 100)
        correct_answer = "yes" if self._is_even(number) else "no"
        return {
            "question": str(number),
            "correct_answer": correct_answer
        }

    def _check_answer(self, question_data, answer):
        return question_data["correct_answer"] == answer.lower()

    @staticmethod
    def _is_even(number: int) -> bool:
        if number % 2 == 0:
            return True
        return False


class GameBrainCalc(Game):
    OPERATIONS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }

    def _get_game_header(self):
        print("What is the result of the expression?")

    def _generate_question(self) -> dict:
        num_1 = self._get_random_number()
        num_2 = self._get_random_number()
        math_sign = random.choice(list(self.OPERATIONS))

        return {
            "question": f"Question: {num_1} {math_sign} {num_2}",
            "correct_answer": str(self.OPERATIONS[math_sign](num_1, num_2))
        }

    def _check_answer(self, question_data, answer):
        return question_data["correct_answer"] == answer.lower()

    def _get_random_number(self) -> int:
        return random.randint(0, 100)

    def _get_random_math_sign(self):
        return random.choice(["+", "-", "*"])

    def get_player_answer(self) -> int:
        answer = None
        while answer is None:
            try:
                answer = int(self._get_answer())
            except (TypeError, ValueError):
                pass
        return answer
