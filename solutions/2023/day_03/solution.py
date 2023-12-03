# puzzle prompt: https://adventofcode.com/2023/day/3

from ...base import StrSplitSolution, answer

def sum_part_numbers(schematic):
    rows = len(schematic)
    cols = len(schematic[0])
    total_sum = 0

    def is_symbol(ch):
        return ch not in "0123456789."

    def find_adjacent_numbers(row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and is_symbol(schematic[r][c]):
                return True
        return False

    for row in range(rows):
        col = 0
        while col < cols:
            if schematic[row][col].isdigit():
                number, start_col = schematic[row][col], col
                while col < cols and schematic[row][col].isdigit():
                    col += 1
                number = int(schematic[row][start_col:col])

                if any(find_adjacent_numbers(row, c) for c in range(start_col, col)):
                    total_sum += number
            else:
                col += 1

    return total_sum

def sum_gear_ratios(schematic):
    rows = len(schematic)
    cols = len(schematic[0])
    total_gear_ratio_sum = 0

    def find_adjacent_numbers(row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        adjacent_numbers = set()

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and schematic[r][c].isdigit():
                number, left, right = schematic[r][c], c - 1, c + 1
                while left >= 0 and schematic[r][left].isdigit():
                    number = schematic[r][left] + number
                    left -= 1
                while right < cols and schematic[r][right].isdigit():
                    number += schematic[r][right]
                    right += 1

                adjacent_numbers.add(int(number))

        return list(adjacent_numbers)

    for row in range(rows):
        for col in range(cols):
            if schematic[row][col] == '*':
                adjacent_numbers = find_adjacent_numbers(row, col)
                if len(adjacent_numbers) == 2:
                    total_gear_ratio_sum += adjacent_numbers[0] * adjacent_numbers[1]

    return total_gear_ratio_sum


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    # @answer(1234)
    def part_1(self) -> int:
        number = sum_part_numbers(self.input)
        return number

    # @answer(1234)
    def part_2(self) -> int:
        number = sum_gear_ratios(self.input)
        return number

