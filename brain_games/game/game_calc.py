import random

from brain_games.game.game_abc import Game


class GameBrainCalc(Game):
    OPERATIONS = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }

    def _get_game_header(self) -> None:
        print("What is the result of the expression?")

    def _generate_question(self) -> dict:
        num_1 = self._get_random_number()
        num_2 = self._get_random_number()
        math_sign = random.choice(list(self.OPERATIONS))

        return {
            "question": f"Question: {num_1} {math_sign} {num_2}",
            "correct_answer": str(self.OPERATIONS[math_sign](num_1, num_2)),
        }

    def _check_answer(self, question_data: dict, answer: str) -> bool:
        return question_data["correct_answer"] == answer.lower()

    def _get_random_number(self) -> int:
        return random.randint(0, 100)

    def _get_random_math_sign(self) -> str:
        return random.choice(["+", "-", "*"])
