import sys
input = lambda : sys.stdin.readline().rstrip()

def check(w):
    alph = [0]*26
    for a in w :
        alph[ord(a)-97] += 1
    return tuple(alph)

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