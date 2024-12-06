#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import time

def processFile(filePath):
    def isValidLetter(r, c, letter):
        if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] != letter:
            return False
        return True

    def checkAround(r, c):
        if isValidLetter(r-1, c-1, "M") and isValidLetter(r-1, c+1, "M") and isValidLetter(r+1, c-1, "S") and isValidLetter(r+1, c+1, "S"):
            return True
        if isValidLetter(r-1, c-1, "S") and isValidLetter(r-1, c+1, "S") and isValidLetter(r+1, c-1, "M") and isValidLetter(r+1, c+1, "M"):
            return True
        if isValidLetter(r-1, c-1, "S") and isValidLetter(r-1, c+1, "M") and isValidLetter(r+1, c-1, "S") and isValidLetter(r+1, c+1, "M"):
            return True
        if isValidLetter(r-1, c-1, "M") and isValidLetter(r-1, c+1, "S") and isValidLetter(r+1, c-1, "M") and isValidLetter(r+1, c+1, "S"):
            return True
        return False


    with open(filePath, 'r') as file:
        lines = file.read().splitlines()

    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0])
    res = 0

    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if grid[r][c] == "A" and checkAround(r, c):
                res += 1
    print("Number of X-MAS: " + str(res))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        startTimer = time.perf_counter()
        file_path = sys.argv[1]
        processFile(file_path)
        endTimer = time.perf_counter()
        print("Execution time: " + str(round(endTimer - startTimer, 5)) + " seconds")
