SAMPLE_MODE = False

filename = 'sample.txt' if SAMPLE_MODE else 'input.txt'

def read_input():
  with open(filename) as f:
    return f.readlines()


def get_ranges():
  return [x.strip().split(',') for x in read_input()]

def main():
  p1 = 0
  p2 = 0
  for [st1,st2] in get_ranges():
    r1 = st1.split('-')
    s1 = set(range(int(r1[0]),int(r1[1]) + 1))
    
    r2 = st2.split('-')
    s2 = set(range(int(r2[0]),int(r2[1]) + 1))
    if len(s1 & s2) == len(s1) or len(s1 & s2) == len(s2):
      p1 +=1
    if len(s1 & s2) > 0:
      p2 += 1
  return f'Part 1: {p1}\nPart 2: {p2}'




if __name__ == '__main__':
  print(main())