from sys import path

with open(path[0] + "/input.txt") as f:
    maze = f.readlines()

def distances_from(start, maze):
    visited = set([(start[0], start[1])])
    queue = [(start[0], start[1], 0, '')]
    routeinfo = {}
    for (x, y, dist, POI) in queue:
        contents = maze[y][x]
        if contents not in ".@1234#" and dist > 0:
            routeinfo[contents] = (dist, POI)
            POI += contents
        visited.add((x, y))
        for d in [(1,0),(0,1),(-1,0),(0,-1)]:
            (newx, newy) = (x + d[0], y + d[1])
            if maze[newy][newx]!='#' and (newx, newy) not in visited:
                queue.append((newx, newy, dist+1, POI))
    return routeinfo

def find_routeinfo(maze):
    routeinfo = {}
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            content = maze[y][x]
            if content in '1234@' or content.islower():
                routeinfo[content] = distances_from((x,y),maze)
    return routeinfo

def part1(maze):
    routeinfo = find_routeinfo(maze)
    keys = set(k for k in routeinfo.keys() if k.islower())
    info = {('@', frozenset()): 0}
    for _ in range(len(keys)):
        nextinfo = {}
        for item in info:
            location, inventory, curdist = item[0], item[1], info[item]
            for newkey in keys:
                if newkey not in inventory:
                    dist, route = routeinfo[location][newkey]
                    reachable = all((c in inventory or c.lower() in inventory) for c in route)
                    if reachable:
                        newdist = curdist + dist
                        newkeys = frozenset(inventory | set((newkey,)))
                        if (newkey, newkeys) not in nextinfo or newdist < nextinfo[(newkey, newkeys)]:
                            nextinfo[(newkey,newkeys)] = newdist
        info = nextinfo
    return min(info.values())

def changeMap(maze):
    maze = [list(line) for line in maze]
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == '@':
                for (dx,dy) in [(0,0),(1,0),(0,1),(-1,0),(0,-1)]:
                    maze[y+dy][x+dx]='#'
                maze[y-1][x-1] = '1'
                maze[y-1][x+1] = '2'
                maze[y+1][x-1] = '3'
                maze[y+1][x+1] = '4'
                return ["".join(line) for line in maze]

def part2(maze):
    maze = changeMap(maze)
    routeinfo = find_routeinfo(maze)
    keys = frozenset(k for k in routeinfo.keys() if k.islower())
    info = {(('1','2','3','4'),frozenset()):0}
    for _ in range(len(keys)):
        nextinfo = {}
        for item in info:
            locations, inventory, curdist = item[0], item[1], info[item]
            for newkey in keys:
                if newkey not in inventory:
                    for robot in range(4):
                        if newkey in routeinfo[locations[robot]]:
                            dist, route = routeinfo[locations[robot]][newkey]
                            reachable = all((c in inventory or c.lower() in inventory) for c in route)
                            if reachable:
                                newdist = curdist + dist
                                newkeys = frozenset(inventory | set((newkey,)))
                                newlocs = list(locations)
                                newlocs[robot] = newkey
                                newlocs = tuple(newlocs)
                                if (newlocs, newkeys) not in nextinfo or newdist < nextinfo[(newlocs, newkeys)]:
                                    nextinfo[(newlocs,newkeys)] = newdist
        info = nextinfo
    return min(info.values())

print(part1(maze))
print(part2(maze))