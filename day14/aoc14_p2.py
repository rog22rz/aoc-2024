import sys
import time

MAP_WIDTH = 101
MAP_HEIGHT = 103 
ITERATIONS = 5000
ERROR_MARGIN = 10

def getSectors(points):
    # Separate into sectors
    nw_sector = 0
    ne_sector = 0
    sw_sector = 0
    se_sector = 0
    for x, y in points:
        if MAP_WIDTH%2 == 1 and int(MAP_WIDTH/2) == int(x):
            continue
        if MAP_HEIGHT%2 == 1 and int(MAP_HEIGHT/2) == int(y):
            continue
        if int(x) < MAP_WIDTH/2:
            if int(y) < MAP_HEIGHT/2:
                nw_sector += 1
            else:
                sw_sector += 1
        else:
            if int(y) < MAP_HEIGHT/2:
                ne_sector += 1
            else:
                se_sector += 1
    return(nw_sector, ne_sector, sw_sector, se_sector)

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
        for j in range(len(points)):
            newX = (int(points[j][0]) + int(velos[j][0]))%MAP_WIDTH
            newY = (int(points[j][1]) + int(velos[j][1]))%MAP_HEIGHT
            if newX < 0:
                newX = MAP_WIDTH + newX
            if newY < 0:
                newY = MAP_WIDTH + newY
            newPoints.append((newX, newY))
        points = newPoints.copy()
        nw, ne, sw, se = getSectors(points)
        if abs(int(nw - sw)) < ERROR_MARGIN and abs(int(ne - se)) < ERROR_MARGIN:
            print("Iteration number: " + str(i))
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
