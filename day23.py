import random, math

def load():
	with open('day23Input.txt') as file:
		data = file.readlines()
		d = [line.strip() for line in data]
	return d

inpt = load()
def part1(inpt):
	inpt = ''.join(inpt)
	inpt = [n for n in inpt.split(',')]
	return 0

def part2(inpt):
	return 0

print(inpt), sep ='\n')