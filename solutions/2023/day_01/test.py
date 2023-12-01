with open(r'D:\Personal\AdventOfCode\solutions\2023\day_01\input.txt') as f:
    text = f.read()

total = 0
words = ['one','two','three','four','five','six','seven','eight','nine']
for line in text.split('\n'):
    first = 0
    for pos in range(len(line)):
        for i, word in enumerate(words):
            i += 1 # because 'one' is in position 0, and so on
            if line[pos:pos+len(word)] == word or line[pos] == str(i):
                if first == 0:
                    first = i
                last = i

    val = first * 10 + last
    total += val

print(total)