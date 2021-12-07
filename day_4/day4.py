import random, math

def load():
    with open('day_4/day4Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()
def part1(inpt):
    won_boards =[]
    def check_winners(b, moves):
        for index, brd in enumerate(b):
            if len(won_boards) != moves:
                pass
            else:
                return total, won_boards
            total = 0
            for x in brd:
                total += sum([int(a) if isinstance(a, str) else 0 for a in x])
            for x in range(5):
                b = list(map(lambda i: isinstance(i, int),  brd[x]))
                if all(b):
                    if index not in won_boards:
                        won_boards.append(index)
                    else:
                        pass
            for y in range(5):
                if isinstance(brd[0][y], int) and isinstance(brd[1][y], int) and isinstance(brd[2][y], int) and isinstance(brd[3][y], int) and isinstance(brd[4][y], int):
                    if index not in won_boards:
                        won_boards.append(index)

        return total, won_boards

    moves = [int(x) for x in inpt.pop(0).split(',')]
    inpt.pop(0)
    boards = []
    board = []
    for element in inpt:
        if element != "":
            to_add = [(x) for x in element.split(" ") if x != ""]
            board.append(to_add)
        else:
            boards.append(board)
            board = []
    boards.append(board)
    
    for count, move in enumerate(moves, start=1):
        for bi, b in enumerate(boards):
            for rowi, row in enumerate(b):
                for _, numb in enumerate(row):
                    boards[bi][rowi] = [int(x) if int(x) == int(move) else x for x in boards[bi][rowi]]
        score, wboards = check_winners(boards, len(moves))
        if len(wboards) == len(boards):
            print(score, move)
            return (score) * move
    print(len(wboards))
    return 0

def part2(inpt):
    return 0

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')