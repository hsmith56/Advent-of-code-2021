import random, math

def load():
    with open('day_1/day1Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()
def part1(inpt):
    inpt = [int(x) for x in inpt] 
    count = 0
    for index, value in enumerate(inpt[0:-1]):
        if value < inpt[index + 1]:
            count += 1
    return count

def part2(inpt):
    inpt = [int(x) for x in inpt] 
    count = 0
    for index, value in enumerate(inpt[0:-2]):
        if sum(inpt[index:index + 3]) < sum(inpt[index + 1:index + 4]):
            count += 1
    return count

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')