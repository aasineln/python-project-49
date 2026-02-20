import random

import prompt


class Game:
    def __init__(self):
        self.player_name = None

    def start(self):
        pass

    def _greeting(self) -> None:
        print("Welcome to the Brain Games!")

    def _get_player_name(self):
        while self.player_name is None or len(self.player_name) == 0:
            self.player_name = prompt.string("May I have your name? ")
        print(f"Hello, {self.player_name}!")


class BrainGames(Game):
    def start(self):
        self._greeting()
        self._get_player_name()


class GameBrainEven(Game):
    def start(self):
        self._greeting()
        self._get_player_name()
        self._start_even_numbers()

    def _start_even_numbers(self) -> None:
        print("Answer \"yes\" if the number is even, otherwise answer \"no\"")
        all_answers_correct = True
        for _ in range(3):
            random_number = random.randint(0, 100)
            print(f"Question: {random_number}")

            answer = prompt.string("Your answer: ")
            if self.is_even(random_number) and answer.lower() == "yes":
                result = "Correct!"
            elif not self.is_even(random_number) and answer.lower() == "no":
                result = "Correct!"
            else:
                result = "Incorrect!"
                all_answers_correct = False
            print(result)

        if all_answers_correct:
            print(f"Congratulations, {self.player_name}!")
        else:
            print(f"Try again, {self.player_name}")

    @staticmethod
    def is_even(number: int) -> bool:
        if number % 2 == 0:
            return True
        return False


class GameBrainCalc(Game):
    def start(self):
        self._greeting()
        self._get_player_name()
        self._start_game_brain_calc()

    def _start_game_brain_calc(self) -> None:
        print("What is the result of the expression?")
        for _ in range(3):
            num_1 = self._get_random_number()
            num_2 = self._get_random_number()
            math_sign = self._get_random_math_sign()

            print(f"Question: {num_1} {math_sign} {num_2}")
            player_answer = self.get_player_answer()
            expected_result = self._get_expected_result(
                num_1=num_1,
                num_2=num_2,
                math_sign=math_sign,
            )

            if player_answer == expected_result:
                print("Correct!")
            else:
                print(
                    f"'{player_answer}' is wrong answer ;(. "
                    f"Correct answer was '{expected_result}'."
                )
                print(f"Let's try again, {self.player_name}!")
                break
            print(f"Congratulations, {self.player_name}!")

    def _get_random_number(self) -> int:
        return random.randint(0, 100)

    def _get_random_math_sign(self):
        return random.choice(["+", "-", "*"])

    def _get_expected_result(
            self, num_1: int, num_2: int, math_sign: str
    ) -> int | None:
        result = None
        match math_sign:
            case "+":
                result = num_1 + num_2
            case "-":
                result = num_1 - num_2
            case "*":
                result = num_1 * num_2
        return result

    def get_player_answer(self) -> int:
        answer = None
        while answer is None:
            try:
                answer = int(prompt.string("Your answer: "))
            except (TypeError, ValueError):
                pass
        return answer