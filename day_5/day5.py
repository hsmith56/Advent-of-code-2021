import random, math

def load():
    with open('day_5/day5Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()
def part1(inpt, p2=False):
    points = {}
    inpt = [([int(z) for z in y[0].split(',')], [int(z) for z in y[1].split(',')]) for y in [list(x.split(' -> ')) for x in inpt]]
    for pair in inpt:
        if pair[0][0] == pair[1][0]:
            for j in range(min(pair[0][1], pair[1][1]), max(pair[0][1], pair[1][1])+1):
                to_add = f'({pair[0][0]},{j})'
                if points.get(to_add):
                    points[(to_add)] += 1
                else:
                    points[(to_add)] = 1

        elif pair[0][1] == pair[1][1]:
            for j in range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0]) + 1):
                to_add = f'({j},{pair[0][1]})'
                if points.get(to_add):
                    points[(to_add)] += 1
                else:
                    points[(to_add)] = 1
        # Part 2
        elif p2:
            if pair[0][0] > pair[1][0]:
                run = 0
                for i in range(max(pair[0][0], pair[1][0]), min(pair[0][0], pair[1][0])-1, -1):
                    if pair[0][1] > pair[1][1]:
                        to_add = f'({i},{abs(pair[0][1] - max(pair[0][0], pair[1][0])+i)})'
                        if points.get(to_add):
                            points[to_add] += 1
                        else:
                            points[to_add] = 1
                    else:
                        to_add = f'({i},{(pair[0][1])+run})'
                        if points.get(to_add):
                            points[to_add] += 1
                        else:
                            points[to_add] = 1
                        run += 1
            else:
                run = 0
                for i in range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0])+1):
                    if pair[0][1] < pair[1][1]:
                        to_add = f'({i},{pair[0][1]+run})'
                        if points.get(to_add):
                            points[to_add] += 1
                        else:
                            points[to_add] = 1
                        run += 1
                    else:
                        to_add = f'({i},{(pair[0][1])+run})'
                        if points.get(to_add):
                            points[to_add] += 1
                        else:
                            points[to_add] = 1
                        run -= 1
        else:
            pass
    
    total = 0
    for v in points.values():
        if v >= 2:
            total += 1
    return total

def part2(inpt):
    return part1(inpt, p2=True)

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')