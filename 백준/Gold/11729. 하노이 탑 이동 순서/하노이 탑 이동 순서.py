N = int(input())

def hanoi(n, s, m, e, lst):
    if n == 1:
        return [[s, e]]
    step1 = hanoi(n-1, s, e, m, lst)
    step2 = [[s, e]]
    step3 = hanoi(n-1, m, s, e, lst)
    return step1+step2+step3

result = hanoi(N, 1, 2, 3, [])
cnt = len(result)

print(cnt)
for i in result:
    print(*i)