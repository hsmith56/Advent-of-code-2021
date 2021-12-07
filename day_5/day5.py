import random, math

def load():
    with open('day_5/example.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()
def part1(inpt):
    points = {}
    stuff = [([int(z) for z in y[0].split(',')], [int(z) for z in y[1].split(',')]) for y in [list(x.split(' -> ')) for x in inpt]]
    for pair in stuff:
        if pair[0][0] == pair[1][0]:
            for j in range(min(pair[0][1], pair[1][1]), max(pair[0][1], pair[1][1])+1):
                if points.get(f'({pair[0][0]},{j})'):
                    points[(f'({pair[0][0]},{j})')] += 1
                else:
                    points[(f'({pair[0][0]},{j})')] = 1
        elif pair[0][1] == pair[1][1]:
            for j in range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0]) + 1):
                if points.get(f'({j},{pair[0][1]})'):
                    points[(f'({j},{pair[0][1]})')] += 1
                else:
                    points[(f'({j},{pair[0][1]})')] = 1
        # Part 2
        else:
            print(pair)
            if pair[0][0] > pair[1][0]:
                for i in range(max(pair[0][0], pair[1][0]), min(pair[0][0], pair[1][0])-1, -1):
                    to_add = f'({i},{abs(pair[0][1] - max(pair[0][0], pair[1][0])+i)})'
                    print(to_add)
                    if points.get(to_add):
                        points[to_add] += 1
                    else:
                        points[to_add] = 1
            else:
                for i in range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0])+1):
                    to_add = f'({i},{abs(pair[0][0] + min(pair[0][0], pair[1][0])-i)})'
                    print(to_add)
                    if points.get(to_add):
                        points[to_add] += 1
                    else:
                        points[to_add] = 1
    print()                
    for y in range(10):
        line = ""
        for x in range(10):
            if f'({x},{y})' in points.keys():
                line = line + str(points[f'({x},{y})'])
            else:
                line = line + "-"
        print(line)
    print()            
    total = 0
    for v in points.values():
        if v >= 2:
            total += 1
    print(len(points.keys()))
    return total

def part2(inpt):
    return 0

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')