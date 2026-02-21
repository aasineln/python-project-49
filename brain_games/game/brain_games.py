from brain_games.game.game_abc import Game


class BrainGames(Game):
    def start(self) -> None:
        self._greeting()
        self._get_player_name()

    def _get_game_header(self) -> None:
        pass

    def _generate_question(self) -> None:
        pass

    def _check_answer(self, question_data: dict, answer: str) -> None:
        pass
