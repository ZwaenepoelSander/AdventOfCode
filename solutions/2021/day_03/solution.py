# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2021/day/3

from ...base import IntSplitSolution, answer


class Solution(IntSplitSolution):
    _year = 2021
    _day = 3

    # @answer(1234)
    def part_1(self) -> int:
        input = str(self.input)
        length = len(input)
        gamma = ""
        
        for j in range(len(input[0])):  # Assuming all strings are of equal length
            zeros = 0
            ones = 0
            for i in range(length):
                if input[i][j] == "0":
                    zeros += 1
                elif input[i][j] == "1":
                    ones += 1
            if zeros > ones:
                gamma += "0"
            else:
                gamma += "1"

        return gamma

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
