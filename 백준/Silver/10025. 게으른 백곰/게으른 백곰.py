import sys
input = sys.stdin.readline

N, K = map(int, input().split())

ice = [0]*2000001

allsum = 0
for _ in range(N):
    g, x = map(int, input().split())
    ice[x] = g
    allsum += g

sumL = [0]*1000001

if K > 500000:
    print(allsum)
    exit()

sumL[K] = sum(ice[0:K*2+1])
result = sumL[K]

for i in range(K+1, 1000000):
    sumL[i] = sumL[i-1] - ice[i-K-1] + ice[i+K]
    if result < sumL[i]:
        result = sumL[i]

print(result)