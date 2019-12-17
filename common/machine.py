memory = []
programPointer = 0


def initMemory(programLineString):
    global memory
    global programPointer
    programPointer = 0
    memory = [int(s) for s in programLineString.split(',')]

def writeToMemory(position, value):
    memory[position] = value

def run(programLineString=None):
    global programPointer
    if (programLineString is not None):
        initMemory(programLineString)

    while True:
        result = executeInstruction()
        if (result is None):
            return memory
        
        moveToNextInstruction()
        if (programPointer is None):
            return memory


def executeInstruction():
    global programPointer
    if (memory[programPointer] == 1):
        return sum(memory[programPointer+1], memory[programPointer+2], memory[programPointer+3])
    if (memory[programPointer] == 2):
        return multiply(memory[programPointer+1], memory[programPointer+2], memory[programPointer+3])
    if (memory[programPointer] == 99):
        return None
    print ("found unknown instruction")
    return None

def sum(a, b, storeAt):
    writeToMemory(storeAt,memory[a] + memory[b])
    return memory[storeAt]

def multiply(a, b, storeAt):
    writeToMemory(storeAt,memory[a] * memory[b])
    return memory[storeAt]


def moveToNextInstruction():
    global programPointer
    if (programPointer + 4 > len(memory)):
        programPointer = None
    else:
        programPointer = programPointer + 4
    
    return programPointer
