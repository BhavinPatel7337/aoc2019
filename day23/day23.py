from sys import path
path.append(path[0] + "/..")
from intcode import IntCode

with open(path[0] + "/input.txt") as f:
    program = [int(x) for x in f.read().strip().split(',')]

def queuePackets(network, packets, i):
    while network[i].output:
        a = network[i].output[0]
        x = network[i].output[1]
        y = network[i].output[2]
        if a in packets:
            packets[a] += [x, y]
        else:
            packets[a] = [x, y]
        network[i].output = network[i].output[3:]

network = {}
packets = {}

for i in range(50):
    network[i] = IntCode(program, i)
    network[i].run(-1)
    queuePackets(network, packets, i)

NAT = [0, 0]
previous = [1, 1]
while previous != NAT:
    previous = NAT
    while packets:
        for p in packets.copy():
            if p == 255:
                NAT = packets[p][-2:]
                print(NAT)
            else:
                output = network[p].run(*packets[p])
                queuePackets(network, packets, p)
            del packets[p]
    packets[0] = NAT