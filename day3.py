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


def recurs_func(inpt, ndx=0, o2=False, co2=False):
    if len(inpt) == 1:
        return int(inpt[0],2)
    dct = {k:{0:0,1:0} for (k) in range(len(inpt[0]))}
    for line in inpt:
        for index, value in enumerate(line):
            dct[index][int(value)] += 1
    next_run = []
    flip = False

    digit_max = max(dct[ndx], key=dct[ndx].get)
    digit_min = min(dct[ndx], key=dct[ndx].get)

    if dct[ndx][0] == dct[ndx][1]:
        flip = True
    if flip:
        digit_max = 1 ^ digit_max

    for i in inpt:
        if o2 and int(i[ndx]) == digit_max:
            next_run.append(i)
        if co2 and int(i[ndx]) == digit_min:
            next_run.append(i)
    return recurs_func(next_run, ndx + 1, o2, co2)

def part2(inpt=inpt):
    dct = {k:{0:0,1:0} for (k) in range(len(inpt[0]))}
    for line in inpt:
        for index, value in enumerate(line):
            dct[index][int(value)] += 1

    oxygen = carbon = []
    
    for i in range(len(inpt[0])):
        digit_max = max(dct[i], key=dct[i].get)
        digit_min = min(dct[i], key=dct[i].get)
        for number in inpt:
            if int(number[i]) == digit_max:
                oxygen.append(number)
            if int(number[i]) == digit_min:
                carbon.append(number)
        return recurs_func(oxygen, o2=True) * recurs_func(carbon, co2=True)

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}') 