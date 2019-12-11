from sys import path
path.append(path[0] + "/..")
from intcode import IntCode
from itertools import permutations

def amplify(program, phase):
    ampA = IntCode(program, phase[0])
    ampB = IntCode(program, phase[1])
    ampC = IntCode(program, phase[2])
    ampD = IntCode(program, phase[3])
    ampE = IntCode(program, phase[4])
    ampA.run(0)
    while not ampE.halted:
        ampB.run(ampA.output[-1])
        ampC.run(ampB.output[-1])
        ampD.run(ampC.output[-1])
        ampE.run(ampD.output[-1])
        ampA.run(ampE.output[-1])
    return ampE.output[-1]

def bruteForcePhase(x, y, program):
    optimal = ([], 0)
    for phase in permutations(list(range(x, y))):
        thruster = amplify(program, phase)
        if optimal[1] < thruster:
            optimal = (phase, thruster)
    return optimal

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

print(bruteForcePhase(0,5, program))
print(bruteForcePhase(5,10, program))