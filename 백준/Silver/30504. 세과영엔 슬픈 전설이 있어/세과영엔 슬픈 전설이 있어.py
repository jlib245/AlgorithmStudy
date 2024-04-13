N = int(input())

inp = list(map(int, input().split()))
A = []
for i in range(N):
    cost = inp[i]
    day = i
    A.append((cost,day))
A.sort()

B = sorted(list(map(int, input().split())))

result = [0]*N
possible = True
for i in range(N):
    must, day = A[i]
    cost = B[i]
    if must <= cost:
        result[day] = cost
    else:
        possible = False
        break

if possible == True:
    print(*result)
else:
    print(-1)