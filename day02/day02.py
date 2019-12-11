from sys import path
path.append(path[0] + "/..")
from intcode import IntCode

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

part1 = IntCode(program)
part1.memory[1] = 12
part1.memory[2] = 2
part1.run()
print(part1.memory[0])

def bruteForce(x, y, value):
    for i in range(x):
        for j in range(y):
            part2 = IntCode(program)
            part2.memory[1] = i
            part2.memory[2] = j
            part2.run()
            if part2.memory[0] == value:
                return 100 * i + j

print(bruteForce(100, 100, 19690720))