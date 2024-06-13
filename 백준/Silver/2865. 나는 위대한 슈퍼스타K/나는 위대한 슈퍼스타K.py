def f(num):
    a = float(format(num, ".1f"))
    b = num - a
    if b >= 0.05:
        return a + 0.1
    else:
        return a
    
N, M, K = map(int, input().split())
max_ = [0 for _ in range(N+1)]
for i in range(M):
    q = list(map(float, input().split()))
    for i in range(len(q)//2):
        num = int(q[2*i-2])
        status = q[2*i-1]
        if max_[num] < status:
            max_[num] = status
max_.sort(reverse=True)

sum_ = 0
for i in range(K):
    sum_ += max_[i]

res = f(sum_)

print(res)