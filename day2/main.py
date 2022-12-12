# A,X: rock 
# B,Y: paper
# C,Z: scissors

winning_map = {
    'A':'Y', 
    'B':'Z', 
    'C':'X'
        }

draw_map = {
    'A':'X',
    'B':'Y',
    'C':'Z'
        }

losing_map = {
    'A':'Z',
    'B':'X',
    'C':'Y'
        }

result_map = {
        'X':0,
        'Y':3,
        'Z':6
        }

part2_map = {
        'A X':3,
        'A Y':1,
        'A Z':2,
        'B X':1,
        'B Y':2,
        'B Z':3,
        'C X':2,
        'C Y':3,
        'C Z':1
        }

def read_input():
    with open('input.txt', 'r') as f:
        return f.readlines()

def part1():
    lines = read_input()
    points = 0
    for line in lines:
        [them,me] = line.split()
        points += list(draw_map.values()).index(me) + 1
        if winning_map[them] == me:
            points += 6
        elif draw_map[them] == me:
            points += 3
    return points

def part2():
    lines = read_input()
    points = 0
    for line in lines:
        points += part2_map[line.rstrip()]
        [them,me] = line.split()
        points += result_map[me]
    return points

if __name__ == '__main__':
    print(part1())
    print(part2())
