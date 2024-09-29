s = input()
dic = {'1':0, '0':0}
dic[s[0]] += 1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        dic[s[i]] += 1
ans = min(dic['0'], dic['1'])
print(ans)