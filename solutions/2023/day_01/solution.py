# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer
import regex as re

def extract_numbers(input_str):
    total=0
    for line in input_str:
        nums=re.findall(r'\d', line)
        number=nums[0]+nums[-1]
        total+=int(number)
    return total

def extract_numbers_part2(input_str):
    total = 0
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for line in input_str:
        first = 0
        last = 0
        for pos in range(len(line)):
            for i, word in enumerate(words):
                if line[pos:pos+len(word)] == word or line[pos] == str(i+1):
                    if first == 0:
                        first = i + 1
                    last = i + 1
        val = first * 10 + last
        total += val
    return total

class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    # @answer(1234)
    def part_1(self) -> int:
        return extract_numbers(self.input)

    # @answer(1234)
    def part_2(self) -> int:
        return extract_numbers_part2(self.input)



    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
