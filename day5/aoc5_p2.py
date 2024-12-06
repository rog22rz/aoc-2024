from io import StringIO
import sys
import time
from collections import defaultdict

def processFile(filePath):
    #def recursion(line, printed):
    #    return (newOrder, isValidOrder)

    def processPages(line):
        printed = set()
        neededPages = set(line)
        newOrder = []
        isValidOrder = True
        for i in range(0, len(line)):
            page = line[i]
            if page not in printed:
                if page in rules:
                    for nextPage in line[i::]:
                        preReqs = set(rules[page])
                        if nextPage in preReqs:
                            isValidOrder = False
                            newOrder.append(nextPage)
                            printed.add(nextPage)
                printed.add(page)
                newOrder.append(page)

        if not isValidOrder:
            print(newOrder)
            return newOrder[int(len(newOrder)/2)]
        return 0

    rules = defaultdict(list)
    middlePageTotal = 0
    with open(filePath, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            if "|" in line:
                parsedRule = line.split("|")
                rules[parsedRule[1]].append(parsedRule[0])
            elif "," in line:
                parsedLine = line.split(",")
                middlePage = int(processPages(parsedLine))
                if middlePage != 0:
                    middlePageTotal += middlePage

    print("The answer is: " + str(middlePageTotal))

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
