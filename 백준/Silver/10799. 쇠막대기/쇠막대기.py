s = input()
ans = 0
cnt = 0
for i in range(len(s)) :
    if s[i] == '(' :
        cnt += 1
    else:
        cnt -= 1
        if s[i-1] == '(': 
            ans += cnt
        else :
            ans += 1
print(ans)