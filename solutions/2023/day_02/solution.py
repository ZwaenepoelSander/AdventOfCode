# puzzle prompt: https://adventofcode.com/2023/day/2

from ...base import StrSplitSolution, answer

def possible_games(input_data):
    # Limits for each color
    limits = {'red': 12, 'green': 13, 'blue': 14}
    sum_of_possible_game_ids = 0

    for line in input_data:
        line = line.replace("Game ", "")
        game_id, parts = line.split(": ")
        game_id = int(game_id)
        parts = parts.split("; ")

        game_possible = True
        for part in parts:
            color_quantity_pairs = part.split(", ")

            for pair in color_quantity_pairs:
                quantity, color = pair.split(" ")
                quantity = int(quantity)

                # Check if the quantity exceeds the limit
                if quantity > limits[color]:
                    game_possible = False
                    break

            if not game_possible:
                break

        if game_possible:
            sum_of_possible_game_ids += game_id
            

    return sum_of_possible_game_ids


def fewest(input_data):
    total_power  = 0
    for line in input_data:
        line = line.replace("Game ", "")
        game_id, parts = line.split(": ")
        game_id = int(game_id)
        parts = parts.split("; ")

        limits = {'red': 0, 'green': 0, 'blue': 0}   
        for part in parts:
            color_quantity_pairs = part.split(", ")

            for pair in color_quantity_pairs:
                quantity, color = pair.split(" ")
                quantity = int(quantity)

                if quantity > limits[color]:
                    limits[color] = quantity
                
        game_power = limits['red'] * limits['green'] * limits['blue']
        total_power += game_power

    return total_power 


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    # @answer(1234)
    def part_1(self) -> int:
        return possible_games(self.input)


    # @answer(1234)
    def part_2(self) -> int:
        return fewest(self.input)
