from sys import path

with open(path[0] + "/input.txt") as f:
    grid = {}
    lines = [line.strip() for line in f.readlines()]
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            grid[(x, y)] = lines[y][x]

def simulate(grid):
    newGrid = {}
    for (x, y) in grid:
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        s = sum([grid.get((x + c[0], y + c[1]), '.') == '#' for c in d])
        if grid[(x, y)] == '#' and s != 1:
            newGrid[(x, y)] = '.'
        elif grid[(x, y)] == '.' and (s == 1 or s == 2):
            newGrid[(x, y)] = '#'
        else:
            newGrid[(x, y)] = grid[(x, y)]
    return newGrid

original = grid.copy()
history = []
while grid not in history:
    history.append(grid)
    grid = simulate(grid)

print(sum([pow(2, y * 5 + x) for x, y in grid if grid[(x, y)] == '#']))

grid3d = {}
for (x, y) in original:
    grid3d[(x, y, 0)] = original[(x, y)]

def addLayers(grid):
    minZ = min([x[2] for x in grid3d.keys()])
    maxZ = max([x[2] for x in grid3d.keys()])
    newMin = sum([grid.get((x, y, minZ), '.') == '#' for x in range(5) for y in range(5)]) > 0
    newMax = sum([grid.get((x, y, maxZ), '.') == '#' for x in range(5) for y in range(5)]) > 0
    for y in range(5):
        for x in range(5):
            if newMin: grid[(x, y, minZ - 1)] = '.'
            if newMax: grid[(x, y, maxZ + 1)] = '.'
    return grid

def recursiveSimulate(grid):
    grid = addLayers(grid)
    newGrid = {}
    for (x, y, z) in grid:
        if not((x, y) == (2, 2)):
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            s = sum([grid.get((x + c[0], y + c[1], z), '.') == '#' for c in d])
            
            o = []
            if x == 0:
                o.append(grid.get((1, 2, z - 1), '.') == '#')
            elif x == 4:
                o.append(grid.get((3, 2, z - 1), '.') == '#')
            if y == 0:
                o.append(grid.get((2, 1, z - 1), '.') == '#')
            elif y == 4:
                o.append(grid.get((2, 3, z - 1), '.') == '#')
            s += sum(o)
            
            i = []
            if (x, y) == (1, 2):
                i += [grid.get((0, a, z + 1), '.') == '#' for a in range(5)]
            elif (x, y) == (2, 1):
                i += [grid.get((a, 0, z + 1), '.') == '#' for a in range(5)]
            elif (x, y) == (2, 3):
                i += [grid.get((a, 4, z + 1), '.') == '#' for a in range(5)]
            elif (x, y) == (3, 2):
                i += [grid.get((4, a, z + 1), '.') == '#' for a in range(5)]
            s += sum(i)

            if grid[(x, y, z)] == '#' and s != 1:
                newGrid[(x, y, z)] = '.'
            elif grid[(x, y, z)] == '.' and (s == 1 or s == 2):
                newGrid[(x, y, z)] = '#'
            else:
                newGrid[(x, y, z)] = grid[(x, y, z)]
    return newGrid

for i in range(200):
    grid3d = recursiveSimulate(grid3d)

print(list(grid3d.values()).count('#'))