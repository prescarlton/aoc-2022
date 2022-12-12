def read_input(): 
    with open('input.txt') as f:
        return f.read().splitlines()

def make_compartments():
  return [[x[:len(x)//2],x[len(x)//2:]] for x in read_input()]

def part1():
    return sum([[(ord(x[0]) - 96 if ord(x[0]) > 96 else ord(x[0])-38) for x in set(y[0]) if x in set(y[1])][0] for y in make_compartments()])

def main():
  for line in make_compartments():
    print(line)


if __name__ == '__main__':
  print(part1())