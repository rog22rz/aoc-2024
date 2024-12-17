import sys
import time

def processFile(filePath):
    with open(filePath, 'r') as file:
        map = file.read().splitlines()

    ROWS = len(map)
    COLS = len(map[0])
    visited = set()
    totalArea = 0
    totalSides = 0
    res = 0

    def computeArea(r, c):
        stack = []
        stack.append((r, c))
        area = 0

        while len(stack) != 0:
            cur = stack.pop()
            if cur in visited:
                continue
            curRow, curCol = cur[0], cur[1]
            visited.add(cur)
            area += 1

            neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for rowDif, colDif in neighbours:
                neighbour = (curRow + rowDif, curCol+ colDif)
                if min(neighbour[0], neighbour[1]) >= 0 and int(neighbour[0]) < ROWS  and int(neighbour[1]) < COLS and map[curRow][curCol] == map[neighbour[0]][neighbour[1]] and (neighbour[0], neighbour[1]) not in visited:
                    stack.append((neighbour[0], neighbour[1]))
        return area

    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) not in visited:
                res += computeArea(r, c) * computeSides(r, c)

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
