import random, math

def load():
    with open('day_9/day9Input.txt') as file:
    #with open('day_9/example.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()
def part1(inpt):
    tot = 0
    for row_num, row in enumerate(inpt):
        for index, number in enumerate(row):
            number = int(number)

            if row_num == 0:
                if index == 0:
                    if number < int(row[index+1]) and number < int(inpt[row_num+1][index]):
                        tot += number + 1
                elif index != len(row) - 1:
                    if number < int(row[index+1]) and number <  int(row[index-1]) and number <  int(inpt[row_num+1][index]):
                        tot += number + 1
                else:
                    if number < int(row[index-1]) and number <  int(inpt[row_num+1][index]):
                        tot += number + 1

            elif row_num < len(inpt) - 1:
                if index == 0:
                    if number < int(row[index+1]) and number <  int(inpt[row_num+1][index]) and number < int(inpt[row_num-1][index]):
                        tot += number + 1
                elif index != len(row) - 1:
                    if number < int(row[index+1]) and number <  int(row[index-1]) and number <  int(inpt[row_num+1][index]) and number < int(inpt[row_num-1][index]):
                        tot += number + 1
                else:
                    if number < int(row[index-1]) and number <  int(inpt[row_num+1][index]) and number < int(inpt[row_num-1][index]):
                        tot += number + 1
            else:
                if index == 0:
                    if number < int(row[index+1]) and number <  int(inpt[row_num-1][index]):
                        tot += number + 1
                elif index != len(row) - 1:
                    if number < int(row[index+1]) and number <  int(row[index-1]) and number <  int(inpt[row_num-1][index]):
                        tot += number + 1
                else:
                    if number < int(row[index-1]) and number <  int(inpt[row_num-1][index]):
                        tot += number + 1
            


    return tot

def part2(inpt):
    return 0

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')
