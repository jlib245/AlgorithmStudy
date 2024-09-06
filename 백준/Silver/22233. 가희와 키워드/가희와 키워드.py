import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
memo = set()
ans = []
for _ in range(N):
    memoKeyWord = input()
    memo.add(memoKeyWord)
for _ in range(M) :
    keyword = input().split(',')
    for x in keyword :
        memo.discard(x)
    ans.append(len(memo))
print(*ans, sep='\n')