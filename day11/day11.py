from sys import path
path.append(path[0] + "/..")
from intcode import IntCode

class Painter:
    def __init__(self, bg):
        self.compass = ['UP', 'RIGHT', 'DOWN', 'LEFT']
        self.x = 0
        self.y = 0
        self.orientation = 0
        self.painted = {(0,0): bg}
    
    def __repr__(self):
        return "Current position: (" + str(self.x) + ", " + str(self.y) + ")\nCurrent orientation: " + self.compass[self.orientation]

    def forward(self):
        if self.orientation == 0:
            self.y -= 1
        elif self.orientation == 1:
            self.x += 1
        elif self.orientation == 2:
            self.y += 1
        elif self.orientation == 3:
            self.x -= 1

    def turn(self, direction):
        if direction == 1:
            self.orientation = (self.orientation + 1) % 4
        else:
            self.orientation = (self.orientation - 1) % 4

    def getColour(self):
        if (self.x, self.y) in self.painted:
            return self.painted[(self.x, self.y)]
        else:
            return 0
    
    def paint(self, colour):
        self.painted[(self.x, self.y)] = colour

    def canvas(self):
        tiles = {
            0: ' ',
            1: '\u2588'
        }
        minX = min(k[0] for k in self.painted.keys())
        maxX = max(k[0] for k in self.painted.keys())
        minY = min(k[1] for k in self.painted.keys())
        maxY = max(k[1] for k in self.painted.keys())
        canvas = ''
        for y in range(minY, maxY + 1):
            for x in range(minX, maxX + 1):
                canvas += tiles[self.painted.get((x,y), 0)]
            canvas += '\n'
        return canvas[:-1]

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

brain = IntCode(program)
robot = Painter(1)
while(not brain.halted):
    brain.run(robot.getColour())
    robot.paint(brain.output[-2])
    robot.turn(brain.output[-1])
    robot.forward()
print(len(robot.painted))
print(robot.canvas())