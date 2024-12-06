from io import StringIO
import sys
import time
from collections import defaultdict

def processFile(filePath):
    def isOrderValid(line):
        printed = set()
        neededPages = set(line)
        for page in line:
            if page in rules:
                for preReq in rules[page]:
                    if preReq in neededPages and preReq not in printed:
                        return False
            printed.add(page)
        return True

    rules = defaultdict(list)
    res = 0
    with open(filePath, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            if "|" in line:
                parsedRule = line.split("|")
                rules[parsedRule[1]].append(parsedRule[0])
            elif "," in line:
                parsedLine = line.split(",")
                if isOrderValid(parsedLine):
                    res += int(parsedLine[int(len(parsedLine)/2)])

    print("The answer is: " + str(res))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    elif sys.argv[1] == "-b":
        totalTime = 0
        iterations = 500
        originalStdout = sys.stdout
        sys.stdout = StringIO()
        for i in range(iterations):
            startTimer = time.perf_counter()
            file_path = sys.argv[2]
            processFile(file_path)
            endTimer = time.perf_counter()
            totalTime += endTimer - startTimer
            print("Execution time: " + str(round(endTimer - startTimer, 5)) + " seconds")
        sys.stdout = originalStdout
        print("Average execution time over " + str(iterations) + " iterations is " + str(round(totalTime/iterations, 5)))
    else:
        startTimer = time.perf_counter()
        file_path = sys.argv[1]
        processFile(file_path)
        endTimer = time.perf_counter()
        print("Execution time: " + str(round(endTimer - startTimer, 5)) + " seconds")
