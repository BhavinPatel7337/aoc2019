from sys import path

with open(path[0] + "/input.txt") as f:
    original = [int(x) for x in f.read().strip()]

signal = original
for _ in range(100):
    newSig = []
    for i in range(len(signal)):
        j = i
        total = 0
        while j < len(signal):
            total += sum(signal[j:j + i + 1])
            j += 2 * i + 2
            total -= sum(signal[j:j + i + 1])
            j += 2 * i + 2
        newSig.append(abs(total) % 10)
    signal = newSig
print(''.join(map(str, signal[:8])))

signal = original * 10000
offset = int(''.join(map(str, original[:7])))
length = len(signal)
for _ in range(100):
    part_sum = 0
    for i in range(offset, length):
        part_sum += signal[i]
    for i in range(offset, length):
        total = part_sum
        part_sum -= signal[i]
        signal[i] = abs(total) % 10

print(''.join(map(str, signal[offset: offset+8])))