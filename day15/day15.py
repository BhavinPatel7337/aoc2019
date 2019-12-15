from sys import path
path.append(path[0] + "/..")
from intcode import IntCode
from os import system

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

class Droid:
    def __init__(self, program, areaMap):
        self.position = (0, 0)
        self.direction = 1
        self.control = IntCode(program)
        self.status = 1
        self.areaMap = areaMap
        self.route = set()
    
    def move(self, direction):
        self.status = self.control.run(direction)[-1]
        if direction == 1:
            newPos = (self.position[0], self.position[1] - 1)
        elif direction == 2:
            newPos = (self.position[0], self.position[1] + 1)
        elif direction == 3:
            newPos = (self.position[0] + 1, self.position[1])
        elif direction == 4:
            newPos = (self.position[0] - 1, self.position[1])
        if self.status == 0:
            self.areaMap[newPos] = 1
            return True
        else:
            self.areaMap[self.position] = 2
            self.areaMap[newPos] = 3
            self.direction = direction
            self.position = newPos
            self.route.add(newPos)
            return False
    
    def left(self):
        if self.direction == 1:
            return 4
        elif self.direction == 2:
            return 3
        elif self.direction == 3:
            return 1
        elif self.direction == 4:
            return 2

    def right(self):
        if self.direction == 1:
            return 3
        elif self.direction == 2:
            return 4
        elif self.direction == 3:
            return 2
        elif self.direction == 4:
            return 1

    def reverse(self):
        if self.direction == 1:
            return 2
        elif self.direction == 2:
            return 1
        elif self.direction == 3:
            return 4
        elif self.direction == 4:
            return 3

    def display(self):
        tiles = {
            0: ' ',
            1: '\u2588',
            2: '.',
            3: 'D',
            4: 'O'
        }
        minX = min(k[0] for k in self.areaMap.keys())
        maxX = max(k[0] for k in self.areaMap.keys())
        minY = min(k[1] for k in self.areaMap.keys())
        maxY = max(k[1] for k in self.areaMap.keys())
        system('cls || clear')
        canvas = ''
        for y in range(minY, maxY + 1):
            for x in range(minX, maxX + 1):
                canvas += tiles[self.areaMap.get((x, y), 0)]
            canvas += '\n'
        print(canvas[:-1])

areaMap = {(0, 0): 3}
droid = Droid(program, areaMap)
while droid.status != 2:
    deadEnd = droid.move(droid.left())
    if deadEnd:
        deadEnd = droid.move(droid.direction)
        if deadEnd:
            deadEnd = droid.move(droid.right())
            if deadEnd:
                droid.direction = droid.reverse()

    droid.display()
routeL = droid.route
areaMap = droid.areaMap

droid = Droid(program, areaMap)
while droid.status != 2:
    deadEnd = droid.move(droid.right())
    if deadEnd:
        deadEnd = droid.move(droid.direction)
        if deadEnd:
            deadEnd = droid.move(droid.left())
            if deadEnd:
                droid.direction = droid.reverse()

    droid.display()
routeR = droid.route
tank = droid.position
oxygen = [tank]
i = -1
while len(oxygen):
    for o in oxygen.copy():
        if areaMap[(o[0] + 1, o[1])] == 2:
            oxygen.append((o[0] + 1, o[1]))
        if areaMap[(o[0] - 1, o[1])] == 2:
            oxygen.append((o[0] - 1, o[1]))
        if areaMap[(o[0], o[1] + 1)] == 2:
            oxygen.append((o[0], o[1] + 1))
        if areaMap[(o[0], o[1] - 1)] == 2:
            oxygen.append((o[0], o[1] - 1))
        droid.areaMap[o] = 4
        oxygen.remove(o)
        droid.display()
    i += 1
print(len(routeL & routeR))
print(i)