from sys import path

def genPath(wire):
    path = []
    x = 0
    y = 0
    path.append((x,y))
    for i in wire:
        if i[0] == 'R':
            length = int(i[1:])
            for j in range(1, length + 1):
                path.append((x + j, y))
            x += length
        elif i[0] == 'L':
            length = int(i[1:])
            for j in range(1, length + 1):
                path.append((x - j, y))
            x -= length
        elif i[0] == 'U':
            length = int(i[1:])
            for j in range(1, length + 1):
                path.append((x, y + j))
            y += length
        elif i[0] == 'D':
            length = int(i[1:])
            for j in range(1, length + 1):
                path.append((x, y - j))
            y -= length
    return path

with open(path[0] + "/input.txt") as f:
    wires = [x.split(',') for x in f.read().strip().split('\n')]

path1 = genPath(wires[0])
path2 = genPath(wires[1])

distances = []
steps = []
for i in set(path1) & set(path2):
    distances.append(abs(i[0]) + abs(i[1]))
    steps.append(path1.index(i) + path2.index(i))
distances.sort()
steps.sort()

print("Shortest Manhattan Distance: " + str(distances[1]))
print("Fewest Combined Steps: " + str(steps[1]))