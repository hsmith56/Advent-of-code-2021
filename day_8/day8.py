import random, math

def load():
    with open('day_8/day8Input.txt') as file:
        data = file.readlines()
        d = [line.strip() for line in data]
    return d

inpt = load()
def part1(inpt):

    
    inpt = [x.split('|')[1].rstrip('\n').strip().split(' ') for x in inpt]
    tot = 0
    for elem in inpt:
        pos_two_or_five, two, three, number_four, fix, six, number_seven, eight, number_nine, pos_zero, pos_one_or_three, four_or_six = '', '', '', '', '', '', '', '', '', '', '',''
        location_mapping = {
            0:0,
            1:1,
            2:2,
            3:3,
            4:4,
            5:5,
            6:6,
            }
        for x in elem:
            if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
                tot += 1
            if len(x) == 2:
                pos_two_or_five = x
            if len(x) == 3:
                number_seven = x
            if len(x) == 4:
                number_four = x
            if len(x) == 7:
                number_eight = x
            
            if pos_two_or_five and number_seven:
                pos_zero = set(pos_two_or_five) ^ set(number_seven)
            if number_seven and number_four:
                pos_one_or_three = (set(number_seven) & set(number_four)) ^ set(number_four) # Either 
            if pos_two_or_five and pos_one_or_three:
                test = set(pos_two_or_five) | pos_one_or_three
                example = [x if set(x) == test else "" for x in elem]
                number_nine = [i for i in example if i][0]
                print(number_nine)
                print(pos_two_or_five, pos_one_or_three)
            if number_nine and number_eight:
                pos_four_or_six = set(number_nine) ^ set(number_eight)
                # print(pos_four_or_six,  number_nine, number_eight)
            
            
                

        #print(elem) 
        
            
                
        # print(location_mapping[0])
        # print(one, seven)
    return tot

def part2(inpt):
    inpt = " ".join(inpt)
    print(inpt)
    output = inpt.strip().split(" | ")


    n = ""
    for o in output.split():
        l = len(o)
        if   l == 2: n += "1"; part1 += 1
        elif l == 4: n += "4"; part1 += 1
        elif l == 3: n += "7"; part1 += 1
        elif l == 7: n += "8"; part1 += 1
        elif l == 5:
            s = set(o)
            if   len(s & d[2]) == 2: n += "3"
            elif len(s & d[4]) == 2: n += "2"
            else:                    n += "5"
        else: # l == 6
            s = set(o)
            if   len(s & d[2]) == 1: n += "6"
            elif len(s & d[4]) == 4: n += "9"
            else:                    n += "0"

    part2 += int(n)

    print(part1)
    print(part2)
    #seven = [1,3,6]
    #one = [3,6]
    #zero = [1,2,3,5,6,7]
    #eight = [1,2,3,4,5,6,7]
    #top = list(set(seven).symmetric_difference(set(one)))
    #middle = list(set(zero).symmetric_difference(set(eight)))
    #return top, middle
    # blah = "testestsetettet.slk"
    # t = blah[-4::]
    # return t 

print(f'Part1: {part1(inpt)}\nPart2: {0}')
