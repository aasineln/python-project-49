import random

from brain_games.game.game_abc import Game


class GameBrainEven(Game):
    def _get_game_header(self) -> None:
        print('Answer "yes" if the number is even, otherwise answer "no".')

    def _generate_question(self) -> dict:
        number = random.randint(0, 100)
        correct_answer = "yes" if self._is_even(number) else "no"
        return {"question": str(number), "correct_answer": correct_answer}

    def _check_answer(self, question_data: dict, answer: str) -> bool:
        return question_data["correct_answer"] == answer.lower()

    @staticmethod
    def _is_even(number: int) -> bool:
        if number % 2 == 0:
            return True
        return False
