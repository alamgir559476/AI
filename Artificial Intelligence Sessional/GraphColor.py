import random as rn
divisions  = ['Dhaka','Mymensingh','Rajshahi','Chattogram','Sylhet','Khulna','Rangpur','Barisal']
adjacentDivision = [
                        [0,1,1,1,0,1,0,1],
                        [1,0,1,1,1,0,1,0],
                        [1,1,0,0,0,1,1,0],
                        [1,1,0,0,1,0,0,1],
                        [0,1,0,1,0,0,0,0],
                        [1,0,1,0,0,0,0,1],
                        [0,1,1,0,0,0,0,1],
                        [1,0,0,1,0,1,0,0]
]
def ConflictCheck(hostDivision,colorCode):
    for i in range(8):
        if adjacentDivision[hostDivision][i] == 1:
            if setColor[i] == colorCode:
                return True
    return False
def DivisionColoring(divisionNumber):
    x = 0
    for x in range(8):
        if(ConflictCheck(divisionNumber,x)):
            continue
        break
    setColor[divisionNumber] = x

colorName = ['Green','White','Orange','Blue','Purple','Yellow','Brown','Violet']
setColor = [99,99,99,99,99,99,99,99]
waitingDivision = [0,1,2,3,4,5,6,7]
for _ in range(8):
    x = rn.choice(waitingDivision)
    DivisionColoring(x)
    waitingDivision.remove(x)
print('Total number of color are used : ',max(setColor)+1)
print('\nColor of Each Division are below: \n')
for i in range(8):
    print(divisions[i]," is color by -> ",colorName[setColor[i]])


