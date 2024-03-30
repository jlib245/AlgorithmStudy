def f(a= list()):
    a.pop()
    return(a)
N, K = map(int, input().split())
G = []
for i in range(N):
    G.append(list(map(int, input().split())))
G.sort(key=f)
R = []
for i in range(N):
    R.append(G[i][0])
result = R.index(K)
while 1:
    if G[result][1:] == G[result-1][1:]:
        result -= 1
    else:
        break
print(result+1)