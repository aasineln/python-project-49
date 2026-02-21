import random

from brain_games.game.game_abc import Game


class GamePrimeNumber(Game):
    def _get_game_header(self) -> None:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')

    def _generate_question(self) -> dict:
        number = self._get_random_number(0, 10)
        is_prime = "yes" if self._is_prime_number(number) else "no"

        return {
            "question": number,
            "correct_answer": is_prime,
        }

    def _check_answer(self, question_data: dict, answer: str) -> bool:
        return question_data["correct_answer"] == answer.lower()

    def _get_random_number(self, num_1: int = 0, num_2: int = 100) -> int:
        return random.randint(num_1, num_2)

    def _is_prime_number(self, number: int) -> bool:
        if number <= 1:
            return False
        for denominator in range(2, number):
            if number % denominator == 0:
                return False
        return True
