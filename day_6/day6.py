import random, math

def load():
    with open('day_6/day6input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()
def part1(inpt, rnge=80):
    inpt = [int(x) for x in inpt[0].split(',')]
    d = {i:0 for i in range(9)}
    d2 = d.copy()
    total = 0
    for x in inpt:
        d[x] = d[x] + 1
    for i in range(rnge):
        for daysleft in d.keys():
            if daysleft > 0 and daysleft <= 6:
                d2[daysleft-1] = d[daysleft]
            elif daysleft == 0:
                d2[8] = d[0]
                d2[7] = d[8]
                d2[6] = d[0] + d[7]
        d = d2.copy()
    for value in d.values():
        total += value
    return total

def part2(inpt):
    return part1(inpt, rnge=256)

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')