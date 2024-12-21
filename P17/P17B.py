import numpy as np

class Program:
    def __init__(self,rA,iSet):
        self.rA = rA
        self.rB = 0
        self.rC = 0
        self.iSet = iSet
        self.ip = 0
        self.out = ''
    
    def getCombo(self,code):
        if code < 4:
            return code
        if code == 4:
            return self.rA
        if code == 5:
            return self.rB
        if code == 6: 
            return self.rC 
    
    def calcNext(self):
        if self.ip >= len(self.iSet):
            return False
        opcode = self.iSet[self.ip]
        combo = self.getCombo(self.iSet[self.ip+1])
        operand = self.iSet[self.ip+1]
        if opcode == 0:
            self.rA = int(self.rA / 2 ** combo)
            self.ip += 2
        elif opcode == 1:
            self.rB = self.rB ^ operand
            self.ip += 2
        elif opcode == 2:
            self.rB = combo % 8
            self.ip += 2
        elif opcode == 3:
            self.ip = (0 if self.rA != 0 else self.ip + 2)
        elif opcode == 4:
            self.rB = self.rB ^ self.rC
            self.ip += 2
        elif opcode == 5:
            self.out += ','
            self.out += str(combo % 8)
            self.ip += 2
        elif opcode == 6:
            self.rB = int(self.rA / 2 ** combo)
            self.ip += 2
        elif opcode == 7:
            self.rC = int(self.rA / 2 ** combo)
            self.ip += 2
        return True
        
def checkOut(out,against):
    return np.array_equal(against,[int(x) for x in out[1:].split(',')])
    
def checkOffset(rAInit,acc):
    program = Program(rAInit,iSet)
    while program.calcNext():
        #print(program.ip,program.rA,program.rB,program.rC)
        pass
    return checkOut(program.out,iSet[len(iSet)-acc:])

def getRange(nums,acc):
    valid = []
    for num in nums:
        num = 8 * num
        for i in range(8):
            if checkOffset(num+i,acc):
                valid.append(num+i)
    return valid
        

iSet = [2,4,1,5,7,5,0,3,4,1,1,6,5,5,3,0]
iSet2 = [0,3,5,4,3,0]

newRange = [0,1,2,3,4,5,6,7]

for acc in range(1,17):
    newRange = getRange(newRange,acc)
    print(newRange)
    print(acc)

print(min(newRange))
#print(checkOffset(25,2))
