from sys import path

with open(path[0] + "/input.txt") as f:
    moves = [line.strip() for line in f.readlines()]

n = 10007
c = 2019
for l in moves:
    if l.startswith('deal into new stack'):
        c = (-c - 1) % n
    elif l.startswith('deal with increment'):
        c = (c * int(l.split(' ')[-1])) % n
    elif l.startswith('cut'):
        c = (c - int(l.split(' ')[-1])) % n
print(c)

n = 119315717514047
c = 2020
a, b = 1, 0
for l in moves:
    if l == 'deal into new stack':
        la, lb = -1, -1
    elif l.startswith('deal with increment '):
        la, lb = int(l[len('deal with increment '):]), 0
    elif l.startswith('cut '):
        la, lb = 1, -int(l[len('cut '):])
    a = (la * a) % n
    b = (la * b + lb) % n

M = 101741582076661
def inv(a, n):
    return pow(a, n-2, n)

Ma = pow(a, M, n)
Mb = (b * (Ma - 1) * inv(a-1, n)) % n

print(((c - Mb) * inv(Ma, n)) % n)