from os import system
from sys import path
path.append(path[0] + "/..")
from intcode import IntCode

def display(output):
    tiles = {
        0: ' ',
        1: '\u2588',
        2: '#',
        3: '@',
        4: '0'
    }
    screen = {(output[i], output[i + 1]): output[i + 2] for i in range(0, len(output), 3)}
    maxX = max(k[0] for k in screen.keys())
    maxY = max(k[1] for k in screen.keys())
    system('cls || clear')
    canvas = ''
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            canvas += tiles[screen.get((x, y), 0)]
        canvas += '\n'
    print(canvas[:-1])
    return screen

def compare(a, b):
    return 0 if b - a == 0 else int((b - a) / abs(b - a))

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

arcade = IntCode(program)
arcade.memory[0] = 2
output = arcade.run()
screen = display(output)
part1 = list(screen.values()).count(2)
while not arcade.halted:
    ball = list(screen.keys())[list(screen.values()).index(4)]
    paddle = list(screen.keys())[list(screen.values()).index(3)]
    output = arcade.run(compare(paddle[0], ball[0]))
    screen = display(output)

print(part1)
print(screen[(-1, 0)])