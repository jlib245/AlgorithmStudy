import sys
input = lambda : sys.stdin.readline().rstrip()

def check(w):
    return ''.join(sorted(w))

N = int(input())
dic = {}
for _ in range(N):
    w = input()
    dic[(w[0], w[-1], check(w))] = w

M = int(input())
sentence = input().split()
ans = []
for w in sentence:
    ans.append(dic[(w[0], w[-1], check(w))])

print(*ans)