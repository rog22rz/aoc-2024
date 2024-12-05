import sys

def processLine(line):
    parsedLine = line.split()

    if(len(parsedLine) <= 1):
        return True

    isIncreasing = int(parsedLine[1]) - int(parsedLine[0]) > 0 
    for i in range(0, len(parsedLine)-1):
        cur = int(parsedLine[i])
        next = int(parsedLine[i+1])
        difference = next - cur
        if(abs(difference) > 3 or difference == 0):
            return False
        if((isIncreasing and difference < 0) or (not isIncreasing and difference > 0)):
            return False
    return True

def processFile(filePath):
    try:
        with open(filePath, 'r') as file:
            safeCount = 0
            for line in file:
                if(processLine(line)):
                    safeCount += 1

            print("The answer is: " + str(safeCount))


    except Exception as e:
        print(f"Error while opening file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        file_path = sys.argv[1]
        processFile(file_path)
