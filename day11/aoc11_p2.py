import sys
import time
from collections import defaultdict

def processFile(filePath):

    with open(filePath, 'r') as file:
        line = file.read().strip().split(" ")

    prevIteration = {}
    currentIteration = {}
    NUMBER_OF_ITERATIONS = 75

    for rock in line:
        currentIteration[rock] = 1 + currentIteration.get(rock, 0)

    for i in range(NUMBER_OF_ITERATIONS):
        prevIteration = currentIteration.copy()
        currentIteration.clear()
        for k, v in prevIteration.items():
            if int(k) == 0:
                currentIteration[str(1)] = v + currentIteration.get(str(1), 0)
            elif len(k) % 2 == 0:
                halfLength = int(len(k)/2)
                firstHalf = int(k[:halfLength])
                secondHalf = int(k[halfLength:])
                currentIteration[str(firstHalf)] = v + currentIteration.get(str(firstHalf), 0)
                currentIteration[str(secondHalf)] = v + currentIteration.get(str(secondHalf), 0)
            else:
                currentIteration[str(int(k)*2024)] = v + currentIteration.get(str(int(k)*2024), 0)

    res = 0

    for _, v in currentIteration.items():
        res += v

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
