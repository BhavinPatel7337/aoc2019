from sys import path
path.append(path[0] + "/..")
from intcode import IntCode
from itertools import combinations
import os

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

def display(droid):
    return ''.join([chr(x) for x in droid.output])

def execute(instructions):
    for i in instructions:
        cmd = [ord(x) for x in i]
        droid.run(*cmd)
    droid.output = []

def drop(droid):
    drop = ['drop coin\n', 'drop dark matter\n', 'drop fuel cell\n', 'drop jam\n', 'drop planetoid\n', 'drop sand\n', 'drop spool of cat6\n', 'drop wreath\n']
    execute(drop)

def bruteforce(droid, items):
    for l in range(1, len(items) + 1):
        for subset in combinations(items, l):
            drop(droid)
            instructions = []
            for s in subset:
                instructions.append('take ' + s + '\n')
            execute(instructions)
            
            attempt = ['inv\n', 'south\n']
            for i in attempt:
                cmd = [ord(x) for x in i]
                droid.run(*cmd)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(display(droid))
            if 'Droids on this ship are lighter' in display(droid):
                print(instructions, 'lighter')
            elif 'Droids on this ship are heavier' in display(droid):
                print(instructions, 'heavier')
            else:
                return

droid = IntCode(program)
instructions = ['west\n', 'north\n', 'take dark matter\n', 'south\n', 'east\n', 'north\n', 'west\n', 'take planetoid\n', 'west\n', 'take spool of cat6\n', 'east\n', 'east\n', 'south\n', 'east\n', 'north\n', 'take sand\n', 'west\n', 'take coin\n', 'north\n', 'take jam\n', 'south\n', 'west\n', 'south\n', 'take wreath\n', 'west\n', 'take fuel cell\n', 'east\n', 'north\n', 'north\n', 'west\n', 'drop coin\n', 'drop dark matter\n', 'drop fuel cell\n', 'drop jam\n', 'drop planetoid\n', 'drop sand\n', 'drop spool of cat6\n', 'drop wreath\n', 'south\n']
execute(instructions)
items = ['jam', 'fuel cell', 'planetoid', 'sand', 'spool of cat6', 'coin', 'dark matter', 'wreath']
bruteforce(droid, items)