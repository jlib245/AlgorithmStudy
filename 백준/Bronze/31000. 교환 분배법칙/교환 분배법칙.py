N = int(input())
cnt = 0
for a in range(-N, N+1):
    if a==0:
        cnt+=(N*2+1)**2
        continue
    for b in range(-N, N+1):
        c = 1 - a - b
        if -N <= c <= N:
            cnt += 1
print(cnt)