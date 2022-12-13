def read_input(): 
    with open('sample.txt') as f:
        return f.read().splitlines()

def make_compartments():
  return [[x[:len(x)//2],x[len(x)//2:]] for x in read_input()]

def part1():
    return sum([[(ord(x[0]) - 96 if ord(x[0]) > 96 else ord(x[0])-38) for x in set(y[0]) if x in set(y[1])][0] for y in make_compartments()])

def make_elf_groups():
  elves = read_input()
  return [elves[i*3:((i*3)+3)]  for i,x in enumerate(elves) if(i*3 < len(elves))]

def part2():
  return sum([[(ord(x[0]) - 96 if ord(x[0]) > 96 else ord(x[0])-38) for x in set(y[0]) if x in set(y[1]) and x in set(y[2])][0] for y in make_elf_groups()])




if __name__ == '__main__':
  print(part2())