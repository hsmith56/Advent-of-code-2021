import random, math

def load():
    with open('day_2/day2Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()
def part1(inpt):
    depth = distance = 0
    for direction in inpt:
        if "forward" in direction:
            value = int(direction.replace("forward ",""))
            distance += value
        elif "up " in direction:
            value = int(direction.replace("up ",""))
            depth -= value
        elif "down" in direction:
            value = int(direction.replace("down ",""))
            depth += value
    return depth * distance

def part2(inpt):
    depth = distance = aim = 0
    for direction in inpt:
        if "forward" in direction:
            value = int(direction.replace("forward ",""))
            distance += value
            depth += value * aim
        elif "up " in direction:
            value = int(direction.replace("up ",""))
            aim -= value
        elif "down" in direction:
            value = int(direction.replace("down ",""))
            aim += value
    return depth * distance

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')