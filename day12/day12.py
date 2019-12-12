from sys import path
#572087463375796
class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Moon:
    def __init__(self, x, y, z):
        self.position = Coordinate(x, y, z)
        self.velocity = Coordinate(0, 0, 0)
        self.initial = Coordinate(x, y, z)

def compare(a, b):
    return 0 if b - a == 0 else int((b - a) / abs(b - a))

def applyGravity(a):
    for b in moons:
        a.velocity.x += compare(a.position.x, b.position.x)
        a.velocity.y += compare(a.position.y, b.position.y)
        a.velocity.z += compare(a.position.z, b.position.z)

def applyVelocity(a):
    a.position.x += a.velocity.x
    a.position.y += a.velocity.y
    a.position.z += a.velocity.z

def calcEnergy():
    total = 0
    for m in moons:
        pot = abs(m.position.x) + abs(m.position.y) + abs(m.position.z)
        kin = abs(m.velocity.x) + abs(m.velocity.y) + abs(m.velocity.z)
        total += pot * kin
    return total

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

with open(path[0] + "/input.txt") as f:
    moons = []
    for line in f.readlines():
        coords = line.strip()[1:-1].split(", ")
        x = int(coords[0].split("=")[1])
        y = int(coords[1].split("=")[1])
        z = int(coords[2].split("=")[1])
        moons.append(Moon(x,y,z))

i = 0
periodX = 0
periodY = 0
periodZ = 0
while (periodX == 0 or periodY == 0 or periodZ == 0):
    if i == 1000: print(calcEnergy())
    [applyGravity(a) for a in moons]
    [applyVelocity(a) for a in moons]
    i += 1
    if [m.initial.x for m in moons] == [m.position.x for m in moons]:
        if [0,0,0,0] == [m.velocity.x for m in moons]:
            if periodX == 0:
                periodX = i
                print("X = " + str(i))

    if [m.initial.y for m in moons] == [m.position.y for m in moons]:
        if [0,0,0,0] == [m.velocity.y for m in moons]:
            if periodY == 0:
                periodY = i
                print("Y = " + str(i))
    
    if [m.initial.z for m in moons] == [m.position.z for m in moons]:
        if [0,0,0,0] == [m.velocity.z for m in moons]:
            if periodZ == 0:
                periodZ = i
                print("Z = " + str(i))

print(int(lcm(lcm(periodX, periodY), periodZ)))