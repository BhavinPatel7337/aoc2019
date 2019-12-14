from sys import path
from math import ceil
from re import findall

with open(path[0] + "/input.txt") as f:
    reactions = {}
    for line in f.readlines():
        x = findall(r'(\d+) (\w+)', line)
        reactions[x[-1][1]] = (int(x[-1][0]), x[:-1])

def getOreReq(fuel_amount):
    total_req = {'FUEL': fuel_amount}
    current_req = ['FUEL']
    while current_req:
        for chemical in current_req:
            quantity, reactants = reactions[chemical]
            factor = ceil(total_req[chemical] / quantity)
            for r_quantity, r_chemical in reactants:
                total_req[r_chemical] = total_req.get(r_chemical, 0) + int(r_quantity) * factor
            total_req[chemical] -= quantity * factor
        current_req = [x for x in total_req if total_req[x] > 0 and x != 'ORE']
    return(total_req['ORE'])

ore = getOreReq(1)
print(ore)

lower = 1e12 // ore
upper = lower * 2
fuel = (upper + lower) // 2
while (upper - lower > 1):
    ore = getOreReq(fuel)
    if ore > 1e12:
        upper = fuel
    elif ore < 1e12:
        lower = fuel
    fuel = (upper + lower) // 2
print(int(fuel))