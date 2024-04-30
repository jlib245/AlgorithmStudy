N = int(input())

cnt = 0
for i in range(N):
    a,b,c = map(int, input().split())
    if a != -1 :
        if b == -1 and c == -1:
            cnt += 1
        elif a <= b :
            if c == -1 or b <= c:
                cnt += 1
print(cnt)