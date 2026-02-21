from abc import ABC, abstractmethod

import prompt


class Game(ABC):
    def __init__(self) -> None:
        self.player_name = None
        self.questions_count = 3

    def start(self) -> None:
        self._greeting()
        self._get_player_name()

        if self._play_rounds():
            self._congratulate()
        else:
            self._loose_output()

    def _play_rounds(self) -> bool:
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
    def _get_game_header(self) -> None:
        pass

    @abstractmethod
    def _generate_question(self) -> None:
        pass

    @abstractmethod
    def _check_answer(self, question_data: dict, answer: str) -> None:
        pass

    def _greeting(self) -> None:
        print("Welcome to the Brain Games!")

    def _get_player_name(self) -> None:
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
