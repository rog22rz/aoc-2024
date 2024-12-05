import sys
import time

def processFile(filePath):
    def isValidLetter(r, c, letter):
        if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] != letter:
            return False
        return True

    def checkRow(r, c):
        res = 0
        if isValidLetter(r, c+1, "M")and isValidLetter(r, c+2, "A") and isValidLetter(r, c+3, "S"):
            res += 1
        if isValidLetter(r, c-1, "M")and isValidLetter(r, c-2, "A") and isValidLetter(r, c-3, "S"):
            res +=1
        return res

    def checkCol(r, c):
        res = 0
        if isValidLetter(r+1, c, "M")and isValidLetter(r+2, c, "A") and isValidLetter(r+3, c, "S"):
            res += 1
        if isValidLetter(r-1, c, "M")and isValidLetter(r-2, c, "A") and isValidLetter(r-3, c, "S"):
            res +=1
        return res

    def checkDiags(r, c):
        res = 0
        if isValidLetter(r+1, c+1, "M")and isValidLetter(r+2, c+2, "A") and isValidLetter(r+3, c+3, "S"):
            res += 1
        if isValidLetter(r-1, c-1, "M")and isValidLetter(r-2, c-2, "A") and isValidLetter(r-3, c-3, "S"):
            res +=1
        if isValidLetter(r+1, c-1, "M")and isValidLetter(r+2, c-2, "A") and isValidLetter(r+3, c-3, "S"):
            res += 1
        if isValidLetter(r-1, c+1, "M")and isValidLetter(r-2, c+2, "A") and isValidLetter(r-3, c+3, "S"):
            res +=1
        return res

    with open(filePath, 'r') as file:
        lines = file.read().splitlines()

    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0])
    res = 0

    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if grid[r][c] == "X":
                res += checkRow(r, c) + checkCol(r, c) + checkDiags(r, c)
    print("Number of XMAS: " + str(res))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        startTimer = time.perf_counter()
        file_path = sys.argv[1]
        processFile(file_path)
        endTimer = time.perf_counter()
        print("Execution time: " + str(round(endTimer - startTimer, 5)) + " seconds")
