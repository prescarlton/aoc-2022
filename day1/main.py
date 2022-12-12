def make_list():
    with open("input.txt") as f:
        content = f.read()
        # loop thru each line, split by a double newline
        # then split each line by a single newline, and convert
        # each line to a list of ints
        elves = [[int(y) for y in x.split()] for x in content.split("\n\n")]
    return elves

def part1():
    # list of lists of calorie counts
    lines = make_list()
    print(max([sum(x) for x in lines]))

def part2():
    lines = make_list()
    counts = [sum(x) for x in lines]
    # get largest 3 numbers
    largest = sorted(counts)[-3:]
    # get sum of those 3 numbers
    print(sum(largest))



if __name__ == "__main__":
    part2()
