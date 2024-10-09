import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
num = []
for _ in range(N):
    s = input()
    NS = ""
    for i in range(len(s)):
        if '0' <= s[i] <= '9' :
            NS += s[i]
        else :
            if NS :
                num.append(int(NS))
                NS = ""
    if NS :
        num.append(int(NS))
num.sort()
print(*num, sep='\n')