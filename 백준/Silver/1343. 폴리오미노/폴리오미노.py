s = input().split('.')
res = ['']*len(s)

for i in range(len(s)):
    A = len(s[i]) // 4 * 4
    B = len(s[i]) % 4
    if B % 2 != 0 :
        print(-1)
        exit()
    res[i] += 'A' * A + 'B' * B

print(*res, sep='.')