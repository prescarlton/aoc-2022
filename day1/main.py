def make_list():
    with open("input.txt") as f:
        content = f.read()
        # loop thru each line, split by a double newline
        # then split each line by a single newline, and convert
        # each line to a list of ints
        elves = [[int(y) for y in x.split()] for x in content.split("\n\n")]
    return elves

def main():
    # list of lists of calorie counts
    lines = make_list()
    print(max([sum(x) for x in lines]))


if __name__ == "__main__":
    main()
