import pytest
from solutions.cube_conundrum import find_possible_games


class TestCubeConundrum:
    @pytest.mark.parametrize(
        "loaded_bag, games_information, possible_games",
        [
            (
                {"red": 12, "green": 13, "blue": 14},
                {
                    1: {0: {"blue": 3, "red": 4}, 1: {"red": 1, "green": 2, "blue": 6}, 2: {"green": 2}},
                    2: {0: {"blue": 1, "green": 2}, 1: {"green": 3, "blue": 4, "red": 1}, 2: {"green": 1, "blue": 1}},
                    3: {
                        0: {"green": 8, "blue": 6, "red": 20},
                        1: {"blue": 5, "red": 4, "green": 13},
                        2: {"green": 5, "red": 1},
                    },
                    4: {
                        0: {"green": 1, "red": 3, "blue": 6},
                        1: {"green": 3, "red": 6},
                        2: {"green": 3, "blue": 15, "red": 14},
                    },
                    5: {0: {"red": 6, "blue": 1, "green": 3}, 1: {"blue": 2, "red": 1, "green": 2}},
                },
                [1, 2, 5],
            )
        ],
    )
    def test_find_possible_games(self, loaded_bag, games_information, possible_games):
        assert find_possible_games(loaded_bag, games_information) == possible_games
