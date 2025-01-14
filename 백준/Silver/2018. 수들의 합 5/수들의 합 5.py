N = int(input())
cnt = 0
for i in range(1, N+1):
    j = i
    sum_ = 0
    while sum_ < N :
        sum_ += j
        j += 1
    if sum_ == N :
        cnt += 1
print(cnt)