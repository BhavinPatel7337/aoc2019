from sys import path
path.append(path[0] + "/..")
from intcode import IntCode

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

robot = IntCode(program)
robot.run()
camera = ''.join([chr(i) for i in robot.output])
print(camera)
points = {}
for y in range(len(camera.splitlines()[:-1])):
    for x in range(len(camera.splitlines()[0])):
        points[(x,y)] = camera.splitlines()[y][x]
alignment = []
for x, y in points:
    if points[(x, y)] != '.' and points.get((x + 1, y), '.') != '.' and points.get((x - 1, y), '.') != '.' and points.get((x, y + 1), '.') != '.' and points.get((x, y - 1), '.') != '.':
        alignment.append(x * y)
print(sum(alignment))

a = [ord(i) for i in "R,10,R,10,R,6,R,4\n"]
b = [ord(i) for i in "R,10,R,10,L,4\n"]
c = [ord(i) for i in "R,4,L,4,L,10,L,10\n"]
mmr = [ord(i) for i in "A,B,A,C,A,B,C,B,C,B\n"]
robot = IntCode(program)
robot.memory[0] = 2
robot.run(*mmr, *a, *b, *c, ord('n'), 10)
print(robot.output[-1])