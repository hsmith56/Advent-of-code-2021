import random, math

def load():
    with open('day_10/day10Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()

def part1(inpt):
    points = { ')': 3, ']':57, '}':1197, '>':25137}
    open_close = { '(':')' , '[':']', '{':'}', '<':'>'}

    look_for_close = []
    tot = 0

    for row in inpt:
        for character in row:
            if character in open_close:
                look_for_close.append(open_close[character])
            else:
                
                if look_for_close[-1] == character:
                    look_for_close.pop(-1)
                else:
                    tot += points[character]
                    break
                
    return tot

def part2(inpt):
    return 0

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')
