import sys
import time
from collections import defaultdict

def isValidPoint(point, maxX, maxY):
    if min(int(point[0]), int(point[1])) >= 0 and int(point[0]) < maxX and int(point[1]) < maxY:
        return True
    return False

def computeAntinode(mainPoint, secondaryPoint):
    antinodeX = 0
    antinodeY = 0 
    distanceX = abs(int(mainPoint[0]) - int(secondaryPoint[0]))
    distanceY = abs(int(mainPoint[1]) - int(secondaryPoint[1]))
    if mainPoint[0] > secondaryPoint[0]:
        antinodeX = mainPoint[0] + distanceX
    else:
        antinodeX = mainPoint[0] - distanceX

    if mainPoint[1] > secondaryPoint[1]:
        antinodeY = mainPoint[1] + distanceY
    else:
        antinodeY = mainPoint[1] - distanceY

    return (antinodeX, antinodeY)


def processFile(filePath):
    coordinates = defaultdict(list)
    occupied = set()
    res = 0

    with open(filePath, 'r') as file:
        lines = file.read().splitlines()
        ROWS = len(lines)
        COLS = len(lines[0])
        for r in range(ROWS):
            for c in range(COLS):
                cellChar = lines[r][c]
                if cellChar != "." and cellChar != "#":
                    coordinates[cellChar].append((c, r))

        for _, points in coordinates.items():
            for i in range(len(points)-1):
                for j in range(i+1, len(points)):
                    antinodeI = computeAntinode(points[i], points[j])
                    newAntinode = antinodeI
                    coef = 2
                    while newAntinode not in occupied and isValidPoint(newAntinode, ROWS, COLS):
                        res += 1
                        occupied.add(newAntinode)
                        newAntinode = (antinodeI[0]*coef, antinodeI[1]*coef)
                        coef *= 2
                    antinodeJ = computeAntinode(points[j], points[i])
                    newAntinode = antinodeJ
                    coef = 2
                    while antinodeJ not in occupied and isValidPoint(newAntinode, ROWS, COLS):
                        res += 1
                        occupied.add(newAntinode)
                        newAntinode = (antinodeJ[0]*coef, antinodeJ[1]*coef)
                        coef *= 2
        print("The answer is: " + str(res))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        startTimer = time.perf_counter()
        file_path = sys.argv[1]
        processFile(file_path)
        endTimer = time.perf_counter()
        print("Execution time: " + str(round(endTimer - startTimer, 5)) + " seconds")
