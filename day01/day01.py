from sys import path

def fuelReq(mass):
    fuel = mass // 3 - 2
    return fuel + fuelReq(fuel) if fuel > 0 else 0

with open(path[0] +"/input.txt") as f:
    modules = [int(x) for x in f.read().splitlines()]

print(sum(x // 3 - 2 for x in modules))
print(sum(fuelReq(x) for x in modules))