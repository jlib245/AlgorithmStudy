import sys
N, M = map(int, input().split())
pokeL = [0]
pokeD = {}
for i in range(1, N+1):
    inpuk = sys.stdin.readline().rstrip()
    pokeL.append(inpuk)
    pokeD[inpuk] = i
for i in range(M):
    q = sys.stdin.readline().rstrip()
    if ord(q[0]) >= 65:
        print(pokeD[q])
    else:
        print(pokeL[int(q)])