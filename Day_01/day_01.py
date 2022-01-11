depthsArray = []
depthIncreases = 0

with open('input', 'r') as depthFile:
    depthsArray = depthFile.readlines()

for i in range(1, len(depthsArray)):
    if int(depthsArray[i]) > int(depthsArray[i-1]):
        depthIncreases += 1

print(depthIncreases)
