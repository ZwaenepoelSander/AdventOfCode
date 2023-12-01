# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2021/day/1

from ...base import IntSplitSolution, answer


def depth_increases(depths: list[int]) -> int:
    depth = 0
    for i in range(len(depths)):
        if i == 0:
            continue
        elif depths[i] > depths[i - 1]:
            depth += 1
    return depth

def depth_sum_increases(depths: list[int]) -> int:
    depth = 0
    for i in range(len(depths)):
        if i == 0:
            continue
        if i < len(depths):
            if (depths[i] + depths[i-1] + depths[i-2]) > (depths[i-1] + depths[i-2] + depths[i-3]):
                depth += 1
    return depth


class Solution(IntSplitSolution):
    _year = 2021
    _day = 1

    # @answer(1234)
    def part_1(self) -> int:
        return depth_increases(self.input)

    # @answer(1234)
    def part_2(self) -> int:
        return depth_sum_increases(self.input)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
