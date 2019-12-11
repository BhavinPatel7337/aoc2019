from sys import path

def parseImage(data, x, y):
    if len(data) % (x * y):
        raise ValueError("Invalid dimensions")
    image = []
    i = 0
    while i < len(data):
        layer = []
        for _ in range(y):
            row = data[i:i+x]
            i += x
            layer.append(row)
        image.append(layer)
    return image

def checksum(image):
    minLayer = (len(image[0]) * len(image[0][0]), 0, 0)
    for z in image:
        zeroes = sum(x.count('0') for x in z)
        ones = sum(x.count('1') for x in z)
        twos = sum(x.count('2') for x in z)
        if zeroes < minLayer[0]:
            minLayer = (zeroes, ones, twos)
    return minLayer[1] * minLayer[2]

def decodeImage(image):
    result = ''
    for y in range(len(image[0])):
        for x in range(len(image[0][0])):
            for z in range(len(image)):
                if image[z][y][x] == '0':
                    result += ' '
                    break
                elif image[z][y][x] == '1':
                    result += '\u2588'
                    break
        result += '\n'
    return result[:-1]

with open(path[0] + "/input.txt") as f:
    data = f.read().strip()

image = parseImage(data, 25, 6)
print(checksum(image))
print(decodeImage(image))