import random, math

def load():
    with open('day_10/day10input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()

def part1(inpt):
    points = { ')': 3, ']':57, '}':1197, '>':25137}
    open_close = { '(':')' , '[':']', '{':'}', '<':'>'}

    tot = 0

    for row in inpt:
        look_for_close = []
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
    points = { ')': 1, ']':2, '}':3, '>':4}
    open_close = { '(':')' , '[':']', '{':'}', '<':'>'}

    tot = []

    for row in inpt:
        look_for_close = []
        abrupt = False
        for character in row:
            if character in open_close:
                look_for_close.append(open_close[character])
            else:
                
                if look_for_close[-1] == character:
                    look_for_close.pop(-1)
                else:
                    abrupt = True
                    break

        look_for_close.reverse()
        if not abrupt: 
            running_tot = 0
            for character in "".join(look_for_close):
                running_tot *= 5
                running_tot += points[character]
            tot.append(running_tot)
            
    tot.sort()
    return tot[int(len(tot)/2)]

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')
