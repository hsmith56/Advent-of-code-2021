import random, math

def load():
    with open('day3Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()
def part1(inpt):
    dct = {k:{0:0,1:0} for (k) in range(len(inpt[0]))}
    for line in inpt:
        for index, value in enumerate(line):
            dct[index][int(value)] += 1
            
    gamma = epsilon = ""
    for i in range(len(inpt[0])):
        digit_max = max(dct[i], key=dct[i].get)
        digit_min = min(dct[i], key=dct[i].get)
        gamma += str(digit_max)
        epsilon += str(digit_min)
    return int(gamma, 2) * int(epsilon, 2)


def part2(inpt):
    return 0

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')