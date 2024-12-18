import sys
import time

def processFile(filePath):

    with open(filePath, 'r') as file:
        lines = file.read().splitlines()

    registerA = lines[0].split(" ")[2]
    registerB = lines[1].split(" ")[2]
    registerC = lines[2].split(" ")[2]
    registers = [registerA, registerB, registerC]
    programInput = lines[4].split(" ")[1].split(",")
    i = [0]

    def getComboOperand(literalOperand):
        match int(literalOperand):
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return registers[0]
            case 5:
                return registers[1]
            case 6:
                return registers[2]
            case _:
                return "ERROR"

    def executeInstruction(opcode, literalOperand):
        match int(opcode):
            case 0:
                registers[0] = int(int(registers[0]) / (2**int(getComboOperand(literalOperand))))
                return -1
            case 1:
                registers[1] = int(registers[1]) ^ int(literalOperand)
                return -1
            case 2:
                registers[1] = int(getComboOperand(literalOperand)) % 8
                return -1
            case 3:
                if registers[0] != 0:
                    i[0] = int(literalOperand)
                    i[0] -= 2
                return -1
            case 4:
                registers[1] = int(registers[1]) ^ int(registers[2])
                return -1
            case 5:
                return int(getComboOperand(literalOperand)) % 8
            case 6:
                registers[1] = int(int(registers[0]) / (2**int(getComboOperand(literalOperand))))
                return -1
            case 7:
                registers[2] = int(int(registers[0]) / (2**int(getComboOperand(literalOperand))))
                return -1
            case _:
                return -1

    output = []
    while i[0] < len(programInput) - 1:
        opcode = programInput[i[0]]
        literalOperand = programInput[i[0]+1]
        instructionResult = executeInstruction(opcode, literalOperand)
        if int(instructionResult) >= 0:
            output.append(str(instructionResult))
        i[0] += 2
    print("The answer is: " + ",".join(output))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        startTimer = time.perf_counter()
        file_path = sys.argv[1]
        processFile(file_path)
        endTimer = time.perf_counter()
        print("Execution time: " + str(round(endTimer - startTimer, 5)) + " seconds")
