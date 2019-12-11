from sys import path
path.append(path[0] + "/..")
from intcode import IntCode

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

part1 = IntCode(program)
part1.run(1)
print(part1.output)
part2 = IntCode(program)
part2.run(5)
print(part2.output)