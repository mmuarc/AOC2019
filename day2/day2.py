import sys
sys.path.append("..")
sys.path.append("../common")
from common import machine

test = "1,0,0,0,99"
print("test:" + test)
print (machine.run(test))

test = "2,3,0,3,99"
print("test:" + test)
print (machine.run(test))

test = "2,4,4,5,99,0"
print("test:" + test)
print (machine.run(test))

test = "1,1,1,4,99,5,6,0,99"
print("test:" + test)
print (machine.run(test))


print ("Part One:")
with open("input.txt", "r") as f:
    result = machine.run(f.readline())
    print(result[0])
# 9581917


print ("Part Two:")
noun = 0
verb = 0
with open("input.txt", "r") as f:
    originalInput = f.readline()
    for noun in range(100):
        for verb in range(100):
            machine.initMemory(originalInput)
            machine.writeToMemory(1,noun)
            machine.writeToMemory(2,verb)
            test2Result = machine.run()
            if (test2Result[0] == 19690720):
                print ("Noun:",noun)
                print ("Verb:",verb)
                print(f"solution: {100 * noun + verb} ")
                break

    
# 25 - 5  :  2505


