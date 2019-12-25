from sys import path
path.append(path[0] + "/..")
from intcode import IntCode

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

def springScript(program, script):
    droid = IntCode(program)
    droid.run()
    script = [ord(x) for x in script]
    droid.run(*script)
    return(droid.output[-1])

part1 = '''NOT A J
NOT C T
AND D T
OR T J
WALK
'''
print(springScript(program, part1))

part2 = '''NOT A J
NOT C T
AND H T
OR T J
NOT B T
AND A T
AND C T
OR T J
AND D J
RUN
'''
print(springScript(program, part2))