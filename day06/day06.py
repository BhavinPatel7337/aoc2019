from sys import path

with open(path[0] + "/input.txt") as f:
    orbit = dict([line.strip().split(')')[::-1] for line in f.readlines()])

def chain(x):
    return {x} | chain(orbit[x]) if x in orbit else {x}

print(sum(len(chain(x)) - 1 for x in orbit))
print(len(chain('YOU') ^ chain('SAN')) - 2)