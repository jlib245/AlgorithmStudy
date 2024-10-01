import sys
input = lambda : sys.stdin.readline().rstrip()

def STA(x):
    memory[x] = AC
    return

def LDA(x):
    global AC
    AC = memory[x]
    return

def BEQ(x):
    global PC
    if AC == 0 :
        PC = x
    return

def NOP(x):
    return

def DEC(x):
    global AC
    if AC == 0 :
        AC = 2**8-1
    else :
        AC -= 1
    return
    

def INC(x):
    global AC
    AC = (AC+1) % (2**8)
    return

def JMP(x):
    global PC
    PC = x
    return

def HLT(x):
    ans.append(bin(AC)[2:].zfill(8))
    return True

query = [STA, LDA, BEQ, NOP, DEC, INC, JMP, HLT]

ans = []
memory = [0]*(2**5)
while 1 :
    PC = 0
    AC = 0
    try :
        for i in range(32):
            s = input()
            memory[i] = int(s, 2)
    except :
        break  
    while 1 :
        q, x = memory[PC] >> 5, memory[PC] % (2**5)
        PC = (PC+1)%32
        if query[q](x) :
            break

for row in ans :
    print(row)