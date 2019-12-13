from sys import path
path.append(path[0] + "/..")
from intcode import IntCode

def display(output):
    screen = {}
    for i in range(0, len(output), 3):
        screen[(output[i], output[i + 1])] = output[i + 2]

    maxX = max(k[0] for k in screen.keys())
    maxY = max(k[1] for k in screen.keys())
    canvas = ''
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            if (x, y) in screen:
                if screen[(x,y)] == 0:
                    canvas += ' '
                elif screen[(x,y)] == 1:
                    canvas += '\u2588'
                elif screen[(x,y)] == 2:
                    canvas += '#'
                elif screen[(x,y)] == 3:
                    canvas += '@'
                elif screen[(x,y)] == 4:
                    canvas += '0'
            else:
                canvas += ' '
        canvas += '\n'
    print(canvas[:-1])
    return screen


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
    if ball[0] < paddle[0]:
        arcade.run(-1)
    elif ball[0] > paddle[0]:
        arcade.run(1)
    else:
        arcade.run(0)
    screen = display(output)

print(part1)
print(screen[(-1, 0)])