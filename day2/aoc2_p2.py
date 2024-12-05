import sys

def validNeighbours(n1, n2, isIncreasing):
    difference = int(n2) - int(n1)
    if abs(difference) > 3 or difference == 0:
        return False
    if (isIncreasing and difference < 0) or (not isIncreasing and difference > 0):
        return False
    return True

def processLine(parsedLine):
    if len(parsedLine) <= 1:
        return True

    errors = 0
    isIncreasing = int(parsedLine[1]) - int(parsedLine[0]) > 0 
    i = 0

    while i < (len(parsedLine) - 1):
        cur = int(parsedLine[i])
        nextNumber = int(parsedLine[i + 1])
        if not validNeighbours(cur, nextNumber, isIncreasing):
            if errors >= 1:
                return False
            if i+2 < len(parsedLine) and not validNeighbours(cur, parsedLine[i + 2], isIncreasing):
                return False
            errors += 1
            i += 1
        i += 1
    return True

def processFile(filePath):
    with open(filePath, 'r') as file:
        safeCount = 0
        for line in file:
            parsedLine = line.split()
            if processLine(parsedLine) or processLine(parsedLine[::-1]):
                safeCount += 1

        print("The answer is: " + str(safeCount))



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        file_path = sys.argv[1]
        processFile(file_path)
