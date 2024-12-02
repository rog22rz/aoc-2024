import sys

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
        res = 0
        hmap = {}
        for i in range(0, len(col_2)):
            hmap[col_2[i]] = 1 + hmap.get(col_2[i], 0)

        for i in range(0, len(col_1)):
            if(col_1[i] in hmap):
                res += int(col_1[i]) * int(hmap[col_1[i]])

        print("The answer is: " + str(res))


    except Exception as e:
        print(f"Error while opening file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        file_path = sys.argv[1]
        processFile(file_path)

