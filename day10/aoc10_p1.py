import sys
import time
from collections import defaultdict

def processFile(filePath):


    with open(filePath, 'r') as file:
        map = file.read().splitlines()
    
    ROWS = len(map)
    COLS = len(map[0])
    res = 0

    def dfs(r, c):
        stack = []
        stack.append((r, c))
        visited = set()
        curRes = 0

        while len(stack) != 0:
            cur = stack.pop()
            curRow, curCol = cur[0], cur[1]
            visited.add(cur)
            if map[curRow][curCol] == "9":
                curRes += 1
                continue

            neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for rowDif, colDif in neighbours:
                neighbour = (curRow + rowDif, curCol+ colDif)
                if min(neighbour[0], neighbour[1]) >= 0 and int(neighbour[0]) < ROWS  and int(neighbour[1]) < COLS and (neighbour[0], neighbour[1]) not in visited and int(map[curRow][curCol]) + 1 == int(map[neighbour[0]][neighbour[1]]):
                    stack.append((neighbour[0], neighbour[1]))
        return curRes

    for r in range(ROWS):
        for c in range(COLS):
            if map[r][c] == "0":
                res += int(dfs(r, c))

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
