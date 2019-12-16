from sys import path

with open(path[0] + "/input.txt") as f:
    original = [int(x) for x in f.read().strip()]

signal = original.copy()
for _ in range(100):
    for i in range(len(signal)):
        j = i
        total = 0
        while j < len(signal):
            total += sum(signal[j:j+i+1])
            j += 2 * (i + 1)
            total -= sum(signal[j:j+i+1])
            j += 2 * (i + 1)
        signal[i] = abs(total) % 10
print(''.join(map(str, signal[:8])))

signal = original.copy() * 10000
offset = int(''.join(map(str, original[:7])))
length = len(signal)
for _ in range(100):
    s = 0
    for i in range(length - 1, offset - 1, -1):
        s += signal[i]
        signal[i] = abs(s) % 10
print(''.join(map(str, signal[offset: offset+8])))