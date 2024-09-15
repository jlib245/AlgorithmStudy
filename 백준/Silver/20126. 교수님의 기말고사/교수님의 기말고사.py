import sys
input = sys.stdin.readline

N, M, S = map(int, input().split())

test = [(0, 0), (S, S)]
for i in range(N) :
    x, y = map(int, input().split())
    test.append((x, x+y))
test.sort()

for i in range(N+1) :
    interval = test[i+1][0] - test[i][1] 
    if interval >= M :
        ans = test[i][1]
        break
else :
    ans = -1
print(ans)