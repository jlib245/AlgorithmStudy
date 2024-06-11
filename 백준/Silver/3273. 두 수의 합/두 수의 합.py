n = int(input())
a = list(map(int, input().split()))
x = int(input())

cnt = 0
lst = [False for _  in range(2000001)]
for i in range(n):
    if a[i] > x:
        continue
    else:
        if lst[x-a[i]]:
            cnt+=1
        else:
            lst[a[i]] = True

print(cnt)