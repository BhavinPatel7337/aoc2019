from sys import path

grid = {}
with open(path[0] + "/input.txt") as f:
    lines = f.readlines()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid[(x, y)] = lines[y][x]

portals = {}
for (x, y) in grid:
    if grid.get((x, y), ' ').isupper():
        if grid.get((x + 1, y), ' ').isupper():
            portal = grid[(x, y)] + grid[(x + 1, y)]
            if grid.get((x + 2, y), ' ') == '.':
                if portal in portals:
                    portals[portal].append((x + 2, y))
                else:
                    portals[portal] = [(x + 2, y)]
            elif grid.get((x - 1, y), ' ') == '.':
                if portal in portals:
                    portals[portal].append((x - 1, y))
                else:
                    portals[portal] = [(x - 1, y)]
        elif grid.get((x, y + 1), ' ').isupper():
            portal = grid[(x, y)] + grid[(x, y + 1)]
            if grid.get((x, y + 2), ' ') == '.':
                if portal in portals:
                    portals[portal].append((x, y + 2))
                else:
                    portals[portal] = [(x, y + 2)]
            elif grid.get((x, y - 1), ' ') == '.':
                if portal in portals:
                    portals[portal].append((x, y - 1))
                else:
                    portals[portal] = [(x, y - 1)]

def isOuter(p, grid):
    outerX = max([x for x, y in grid.keys()]) - 3
    outerY = max([y for x, y in grid.keys()]) - 2
    if p[0] == 2 or p[1] == 2 or p[0] == outerX or p[1] == outerY:
        return True
    else:
        return False

def traverse(start, goal, grid, portals):
    visited = set()
    accessible = set([(start, 0)])
    distance = 0
    while accessible:
        for i in accessible.copy():
            pos, level = i
            if pos == goal and level == 0:
                return distance
            x, y = pos
            if grid[(x + 1, y)] == '.' and ((x + 1, y), level) not in visited:
                accessible.add(((x + 1, y), level))
            if grid[(x - 1, y)] == '.' and ((x - 1, y), level) not in visited:
                accessible.add(((x - 1, y), level))
            if grid[(x, y + 1)] == '.' and ((x, y + 1), level) not in visited:
                accessible.add(((x, y + 1), level))
            if grid[(x, y - 1)] == '.' and ((x, y - 1), level) not in visited:
                accessible.add(((x, y - 1), level))
            
            for p in portals.values():
                if pos == p[0]:
                    if isOuter(p[0], grid):
                        if level != 0:
                            if (p[1], level - 1) not in visited:
                                accessible.add(((p[1]), level - 1))
                    else:
                        if (p[1], level + 1) not in visited:
                            accessible.add(((p[1]), level + 1))
                elif pos == p[1]:
                    if isOuter(p[1], grid):
                        if level != 0:
                            if (p[0], level - 1) not in visited:
                                accessible.add(((p[0]), level - 1))
                    else:
                        if (p[0], level + 1) not in visited:
                            accessible.add(((p[0]), level + 1))

            visited.add(i)
            accessible.remove(i)
        distance += 1

start = portals['AA'][0]
del portals['AA']
goal = portals['ZZ'][0]
del portals['ZZ']
print(traverse(start, goal, grid, portals))