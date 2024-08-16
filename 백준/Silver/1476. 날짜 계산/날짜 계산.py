E, S, M = map(int, input().split())
i = 0
while not (i % 15 == E-1 and i % 28 == S-1 and i % 19 == M-1) :
    i += 1
ans = i+1
print(ans)