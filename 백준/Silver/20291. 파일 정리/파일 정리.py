from collections import defaultdict
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

dic = defaultdict(int)
for i in range(N):
    fileName, extension = input().split('.')
    dic[extension] += 1

printSequence = sorted(list(dic.keys()))

for i in printSequence:
    print(i, dic[i])