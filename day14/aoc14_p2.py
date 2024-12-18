import sys
import time

MAP_WIDTH = 101
MAP_HEIGHT = 103 
ITERATIONS = 20000

def printMap(points):
    grid = [['.' for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)] 
    for x, y in points:
        grid[int(y)][int(x)] = "#"
    for row in grid:
        print(" ".join(row))
    print()

def getPoint(line):
    points = line.split("=")[1].split(",")
    return (points[0], points[1])

def processFile(filePath):

    points = []
    velos = []
    validIteration = 0

    with open(filePath, 'r') as file:
        lines = file.read().splitlines()
    
    # Parse input
    for line in lines:
        splittedLine = line.split(" ")
        points.append(getPoint(splittedLine[0]))
        velos.append(getPoint(splittedLine[1]))

    # Move robots around
    for i in range(ITERATIONS):
        newPoints = []
        rowsMap = {}
        maxN = 0
        minN = 999
        for j in range(len(points)):
            newX = (int(points[j][0]) + int(velos[j][0]))%MAP_WIDTH
            newY = (int(points[j][1]) + int(velos[j][1]))%MAP_HEIGHT

            newPoints.append((newX, newY))
            keyPoint = newY
            rowsMap[keyPoint] = rowsMap.get(keyPoint, 0) + 1
            maxN = max(rowsMap[newY], maxN)
            minN = min(rowsMap[newY], minN)
        points = newPoints.copy()

        # Heurisitcs
        if maxN - minN > 20:
            print("Iteration number: " + str(i))
            print("Max: " + str(maxN))
            print("Min: " + str(minN))
            validIteration += 1
            printMap(points)

    print("Number of valid iteration: " + str(validIteration))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        startTimer = time.perf_counter()
        file_path = sys.argv[1]
        processFile(file_path)
        endTimer = time.perf_counter()
        print("Execution time: " + str(round(endTimer - startTimer, 5)) + " seconds")
