def checkPassword(pw):
    if len(str(pw)) != 6:
        return False
    currentDigit = ''
    nextDigit = ''
    adjacentDigits = False
    repeatLength = 1
    repeatLengths = []
    for j in range(5):
        currentDigit = str(pw)[j]
        nextDigit = str(pw)[j + 1]
        if currentDigit > nextDigit:
            return False
        else:
            if currentDigit == nextDigit:
                repeatLength += 1
                adjacentDigits = True
            else:
                repeatLengths.append(repeatLength)
                repeatLength = 1
    repeatLengths.append(repeatLength)
    return adjacentDigits and 2 in repeatLengths

print(sum(checkPassword(i) for i in range(307237, 769059)))