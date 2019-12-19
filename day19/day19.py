from sys import path
path.append(path[0] + "/..")
from intcode import IntCode

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

def inBeam(program, x, y):
    drone = IntCode(program)
    return drone.run(x, y)[-1] == 1

def part1(program):
    return sum([inBeam(program, x, y) for x in range(50) for y in range(50)])

def part2(program):
    x = 0
    y = 100
    while True:
        while not inBeam(program, x, y):
            x += 1
        if inBeam(program, x + 99, y - 99):
            return 10000 * x + (y - 99)
        else:
            y += 1

print(part1(program))
print(part2(program))