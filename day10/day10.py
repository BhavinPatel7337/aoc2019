from sys import path
from math import hypot, atan2

with open(path[0] + "/input.txt") as f:
    asteroidMap = [line.strip() for line in f.readlines()]

asteroids = []
for y in range(len(asteroidMap)):
    for x in range(len(asteroidMap[y])):
        if asteroidMap[y][x] == '#': asteroids.append((x,y))

visible = [len(set([atan2(i[0] - a[0], i[1] - a[1]) for i in asteroids])) for a in asteroids]

optimal = asteroids[visible.index(max(visible))]
print(optimal, max(visible))

locations = {a: (hypot(a[0] - optimal[0], a[1] - optimal[1]), atan2(a[0] - optimal[0], a[1] - optimal[1])) for a in asteroids}
locations = {k: v for k, v in sorted(locations.items(), key=lambda item: item[1][0])}
locations = {k: v for k, v in sorted(locations.items(), reverse=True, key=lambda item: item[1][1])}
del locations[optimal]

count = 0
while locations:
    vaporised, last = [], 0
    for x, y in locations.keys():
        if last != locations[(x,y)][1]:
            count += 1
            if count == 200: print(x * 100 + y)
            last = locations[(x,y)][1]
            vaporised.append((x,y))
    [locations.pop(a) for a in vaporised]