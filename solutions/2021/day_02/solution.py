# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2021/day/2

from ...base import StrSplitSolution, answer
        


class Solution(StrSplitSolution):
    _year = 2021
    _day = 2

    # @answer(1234)
    def part_1(self) -> int:
        input = self.input
        depth = 0
        horizontal = 0
        for i in input:
            if "forward" in i:
                i = i.replace("forward", "")
                i = int(i)
                horizontal += i
            elif "down" in i:
                i = i.replace("down", "")
                i = int(i)
                depth += i
            elif "up" in i:
                i = i.replace("up", "")
                i = int(i)
                depth -= i
        return horizontal * depth

    # @answer(1234)
    def part_2(self) -> int:
        input = self.input
        aim = 0
        depth = 0
        horizontal = 0
        for i in input:
            if "forward" in i:
                i = i.replace("forward", "")
                i = int(i)
                horizontal += i
                depth += aim*i
            elif "down" in i:
                i = i.replace("down", "")
                i = int(i)
                aim += i
            elif "up" in i:
                i = i.replace("up", "")
                i = int(i)
                aim -= i
        return horizontal * depth

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
