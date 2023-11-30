# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2021/day/1

from ...base import IntSplitSolution, answer


def depthIncreases(depths: list[int]) -> int:
    depth = 0
    for i in range(len(depths)):
        if i == 0:
            continue
        elif depths[i] > depths[i - 1]:
            depth += 1
    return depth


class Solution(IntSplitSolution):
    _year = 2021
    _day = 1

    # @answer(1234)
    def part_1(self) -> int:
        return depthIncreases(self.input)

    # @answer(1234)
    def part_2(self) -> int:
        pass       

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
