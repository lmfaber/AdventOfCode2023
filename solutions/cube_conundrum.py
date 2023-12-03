import math


def parse_input(game_information: list[str]):
    games: dict[dict[str, int]] = {}
    for i, line in enumerate(game_information, 1):
        games[i] = {}
        line: str = line.rstrip("\n").split(": ")[-1]
        for j, set in enumerate(line.split("; ")):
            games[i][j] = {}
            for drawing in set.split(", "):
                number_cubes, cube_color = drawing.split()
                games[i][j][cube_color] = int(number_cubes)
    return games


def find_possible_games(loaded_bag, games_info):
    possible_games: list[int] = []
    for number_game, set in games_info.items():
        is_possible_game: bool = True
        for number_set, drawing in set.items():
            for cube_color, number_cubes in drawing.items():
                if loaded_bag[cube_color] < number_cubes:
                    is_possible_game = False
        if is_possible_game:
            possible_games.append(number_game)
    return possible_games


def find_minimum_possible_sets(games_information: dict):
    power_of_games: list[int] = []
    for number_game, game_set in games_information.items():
        min_cubes = {}
        for number_set, drawing in game_set.items():
            for cube_color, number_cubes in drawing.items():
                min_cubes[cube_color] = max(number_cubes, min_cubes.get(cube_color, 0))

        power_of_set = math.prod(min_cubes.values())
        print(min_cubes, power_of_set)
        power_of_games.append(power_of_set)
    return power_of_games


def main():
    """Main method."""
    with open("input_files/cube_conundrum.txt", "r", encoding="utf-8") as reader:
        game_information: list[str] = [line.rstrip("\n") for line in reader.readlines()]
    games_info = parse_input(game_information)
    loaded_bag: dict[str, int] = {"red": 12, "green": 13, "blue": 14}
    possible_games = find_possible_games(loaded_bag, games_info)
    print("Part 1:")
    print(f"The sum of possible games is {sum(possible_games)}.")

    minimum_possible_sets = find_minimum_possible_sets(games_info)
    print("Part 2:")
    print(f"The sum of the powers of the sets is {sum(minimum_possible_sets)}.")


if __name__ == "__main__":
    main()
