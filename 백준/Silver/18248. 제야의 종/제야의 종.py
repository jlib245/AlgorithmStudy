import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
a = []
cnt = []
for i in range(N):
    s = list(map(int, input().split()))
    cnt.append(sum(s))
    a.append((s,i))


a.sort(key=lambda x : cnt[x[1]])

for i in range(N-1):
    for j in range(M):
        far = a[i][0][j]
        near = a[i+1][0][j]
        if far and not near :
            print("NO")
            exit()
print("YES")