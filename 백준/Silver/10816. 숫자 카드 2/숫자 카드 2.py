import sys
input = sys.stdin.readline

N = int(input())
sg= list(map(int, input().split()))

dic = dict()
for i in range(N):
    if sg[i] in dic.keys():
        dic[sg[i]] += 1
    else:
        dic[sg[i]] = 1

M = int(input())
lst = list(map(int, input().split()))

result = []
for i in range(M):
    if lst[i] in dic.keys():
        result.append(dic[lst[i]])
    else:
        result.append(0)
print (*result)