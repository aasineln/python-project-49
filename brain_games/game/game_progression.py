import random

from brain_games.game.game_abc import Game


class GameProgression(Game):
    def __init__(self):
        super().__init__()
        self._progression_length = 10

    def _get_game_header(self) -> None:
        print("What number is missing in the progression?")

    def _generate_question(self) -> dict:
        first_number = self._get_random_number(0, 10)
        progression_step = self._get_random_number(1, 10)
        hidden_index = self._get_random_number(0, self._progression_length - 1)

        progression = []
        hidden_number = None
        for index in range(self._progression_length):
            progression_number = str(first_number + index * progression_step)

            if index == hidden_index:
                progression.append("..")
                hidden_number = progression_number
            else:
                progression.append(progression_number)

        return {
            "question": " ".join(progression),
            "correct_answer": hidden_number,
        }

    def _check_answer(self, question_data: dict, answer: str) -> bool:
        return question_data["correct_answer"] == answer.lower()

    def _get_random_number(self, num_1: int = 0, num_2: int = 100) -> int:
        return random.randint(num_1, num_2)
