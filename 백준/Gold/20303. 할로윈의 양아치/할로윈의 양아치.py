import sys
input = lambda : sys.stdin.readline()

def find(x):
    while parent[x] != x :
        x = parent[x]
    return x

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if x < y :
        parent[y] = x
        candy[x] += candy[y]
        candy[y] = 0
        people[x] += people[y]
        people[y] = 0
    else :
        parent[x] = y
        candy[y] += candy[x]
        candy[x] = 0
        people[y] += people[x]
        people[x] = 0
    return

N, M, K =map(int, input().split())

candy = [0] + list(map(int,input().split()))
people = [0] + [1]*N
parent = [i for i in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    union(x,y)

groupcnt = 0
groupCandy = []
groupPeople = []
for i in range(1, N+1):
    if candy[i] :
        groupcnt += 1
        groupCandy.append(candy[i])
        groupPeople.append(people[i])
'''
dp[i][j] = i번째 친구 그룹까지 j명 이하의 아이들에게 뺏는 최대의 사탕의 수
'''
dp = [[0]*K for i in range(groupcnt)]
newPeople = groupPeople[0]
newCandy = groupCandy[0]
for j in range(newPeople, K):
    dp[0][j] = newCandy
for i in range(1, groupcnt):
    newPeople = groupPeople[i]
    newCandy = groupCandy[i]
    for j in range(1, K):
        if j >= newPeople :
            dp[i][j] = max(dp[i-1][j-newPeople] + newCandy, dp[i-1][j])
        else :
            dp[i][j] = dp[i-1][j]

ans = max(dp[groupcnt-1])
print(ans)