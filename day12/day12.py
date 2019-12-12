from sys import path
from math import gcd
from re import search

class Moon:
    def __init__(self, x, y, z):
        self.position = [x, y, z]
        self.velocity = [0, 0, 0]

def compare(a, b):
    return 0 if b - a == 0 else int((b - a) / abs(b - a))

def applyGravity(a):
    for b in moons:
        a.velocity[0] += compare(a.position[0], b.position[0])
        a.velocity[1] += compare(a.position[1], b.position[1])
        a.velocity[2] += compare(a.position[2], b.position[2])

def applyVelocity(a):
    a.position[0] += a.velocity[0]
    a.position[1] += a.velocity[1]
    a.position[2] += a.velocity[2]

def calcEnergy():
    pot = [abs(m.position[0]) + abs(m.position[1]) + abs(m.position[2]) for m in moons]
    kin = [abs(m.velocity[0]) + abs(m.velocity[1]) + abs(m.velocity[2]) for m in moons]
    return sum([a * b for a, b in zip(pot, kin)])

def lcm(a, b):
    return a * b // gcd(a, b)

with open(path[0] + "/input.txt") as f:
    moons = []
    for line in f.readlines():
        a = search(r'<x=(\-?\d+), y=(\-?\d+), z=(\-?\d+)>', line)
        moons.append(Moon(int(a.group(1)), int(a.group(2)), int(a.group(3))))

t, periodX, periodY, periodZ = 0, 0, 0, 0
while not (periodX and periodY and periodZ):
    if t == 1000: print(calcEnergy())
    [applyGravity(a) for a in moons]
    [applyVelocity(a) for a in moons]
    t += 1
    if [0, 0, 0, 0] == [m.velocity[0] for m in moons] and not periodX: periodX = t * 2
    if [0, 0, 0, 0] == [m.velocity[1] for m in moons] and not periodY: periodY = t * 2
    if [0, 0, 0, 0] == [m.velocity[2] for m in moons] and not periodZ: periodZ = t * 2

print(lcm(lcm(periodX, periodY), periodZ))