sum = 0
complexsum = 0
file = open("input.txt","r")
line = file.readline()

def complexfuel(fuel):
    result = 0
    while fuel > 0:
        fuel = int((fuel / 3) - 2)
        if (fuel < 0):
            break
        result = result+fuel
    return result

while line:
    sum = sum + int(int(line)/3) - 2
    complexsum = complexsum + complexfuel(int(line))
    line = file.readline()

print (sum)
print (complexsum)