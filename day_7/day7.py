import random, math

def load():
    with open('day_7/day7Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()
def part1(inpt):
    inpt = [int(x) for x in inpt[0].split(',')]
    dct = {i:0 for i in range(min(inpt), max(inpt)+1)}
    for i in range(min(inpt), max(inpt)+1):
        for element in inpt:
            if dct.get(i):
                dct[i] += abs(i - element)
            else:
                dct[i] = abs(i - element)
    min_value = min(dct.values())
    return min_value

def part2(inpt):
    inpt = [int(x) for x in inpt[0].split(',')]
    dct = {i:0 for i in range(min(inpt), max(inpt)+1)}
    for i in range(min(inpt), max(inpt)+1):
        for element in inpt:
            if dct.get(i):
                dct[i] += sum([i for i in range(abs(i - element)+1)])
            else:
                dct[i] = sum([i for i in range(abs(i - element)+1)])
    min_value = min(dct.values())
    return min_value

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')