C = int(input())
s = input()
R = len(s) // C
lst = ['' for _ in range(R)]
for i in range(R):
    if i % 2 == 0 :
        lst[i] = s[C*i:C*(i+1)]
    else :
        lst[i] = s[C*i:C*(i+1)][::-1]

ans = ''
for c in range(C):
    for r in range(R):
        ans += lst[r][c]
print(ans)