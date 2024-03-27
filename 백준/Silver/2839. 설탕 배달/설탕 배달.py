N = int(input())
if N < 5:
    a = [-1,-1,-1,1,-1,1]
else :
    a = [-1]*(N+1)
    a[3] = 1
    a[5] = 1
    if N > 5:
        for i in range(6, N+1):
            if a[i-3] != -1 or a[i-5] != -1:
                if a[i-3] == -1:
                    a[i] = a[i-5] + 1
                elif a[i-5] == -1:
                    a[i] = a[i-3] + 1
                else :
                    a[i] = min(a[i-5], a[i-3]) + 1
print(a[N])