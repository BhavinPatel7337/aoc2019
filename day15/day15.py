import os
from sys import path
path.append(path[0] + "/..")
from intcode import IntCode

class Droid:
    def __init__(self, program):
        self.position = (0, 0)
        self.direction = 1
        self.control = IntCode(program)
        self.status = 1
        self.route = set()
    
    def move(self, direction):
        self.status = self.control.run(direction)[-1]
        p = lambda x, y: (self.position[0] + x, self.position[1] + y)
        if direction == 1: newPos = p(0, -1)
        elif direction == 2: newPos = p(0, 1)
        elif direction == 3: newPos = p(1, 0)
        elif direction == 4: newPos = p(-1, 0)
        if self.status == 0:
            areaMap[newPos] = 1
            return True
        else:
            areaMap[self.position] = 2
            areaMap[newPos] = 3
            self.direction = direction
            self.position = newPos
            self.route.add(newPos)
            return False
    
    def left(self):
        d = {1: 4, 2: 3, 3: 1, 4: 2}
        return d[self.direction]

    def right(self):
        d = {1: 3, 2: 4, 3: 2, 4: 1}
        return d[self.direction]

    def reverse(self):
        d = {1: 2, 2: 1, 3: 4, 4: 3}
        return d[self.direction]

    def search(self, mode):
        while self.status != 2:
            if mode == 'left':
                priority = [self.left(), self.right()]
            elif mode == 'right':
                priority = [self.right(), self.left()]
            if self.move(priority[0]) and self.move(self.direction) and self.move(priority[1]):
                self.direction = self.reverse()
            display(areaMap)

def display(areaMap):
    tiles = {
        0: ' ',
        1: '\u2588',
        2: '.',
        3: 'D',
        4: 'O'
    }
    minX = min(k[0] for k in areaMap.keys())
    maxX = max(k[0] for k in areaMap.keys())
    minY = min(k[1] for k in areaMap.keys())
    maxY = max(k[1] for k in areaMap.keys())
    os.system('cls' if os.name == 'nt' else 'clear')
    canvas = ''
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            canvas += tiles[areaMap.get((x, y), 0)]
        canvas += '\n'
    print(canvas[:-1])

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

areaMap = {}
droidL = Droid(program)
droidL.search('left')
droidR = Droid(program)
droidR.search('right')

tank = droidL.position
oxygen = [tank]
i = -1
while len(oxygen):
    for o in oxygen.copy():
        p = lambda x, y: (o[0] + x, o[1] + y)
        if areaMap[p(1, 0)] == 2: oxygen.append(p(1, 0))
        if areaMap[p(-1, 0)] == 2: oxygen.append(p(-1, 0))
        if areaMap[p(0, 1)] == 2: oxygen.append(p(0, 1))
        if areaMap[p(0, -1)] == 2: oxygen.append(p(0, -1))
        areaMap[o] = 4
        oxygen.remove(o)
    display(areaMap)
    i += 1
print(len(droidL.route & droidR.route))
print(i)