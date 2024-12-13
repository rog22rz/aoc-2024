import sys
import time

col_1 = []
col_2 = []

def processLine(line):
    parsedLine = line.split()
    col_1.append(parsedLine[0])
    col_2.append(parsedLine[1])

def processFile(filePath):
    try:
        with open(filePath, 'r') as file:
            for line in file:
                processLine(line)
        col_1.sort()
        col_2.sort()
        res = 0
        for i in range(0, len(col_1)):
            res += abs(int(col_1[i]) - int(col_2[i]))
        print("The answer is: " + str(res))


    except Exception as e:
        print(f"Error while opening file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        startTimer = time.perf_counter()
        file_path = sys.argv[1]
        processFile(file_path)
        endTimer = time.perf_counter()
        print("Execution time: " + str(round(endTimer - startTimer, 5)) + " seconds")

