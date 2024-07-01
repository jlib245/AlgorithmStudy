from collections import defaultdict
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()

sum = 0
dic = defaultdict(int)
mostFreq = 0
for i in lst:
    dic[i] += 1
    sum += i
    if mostFreq < dic[i]:
        mostFreq = dic[i]

avrg = round(sum/N)
mid = lst[N//2]
frequen = 0
for i in range(N):
    if dic[lst[i]] == mostFreq:
        if not frequen:
            frequen = lst[i]
        elif frequen == lst[i]:
            continue
        else:
            frequen = lst[i]
            break

cvrg = lst[N-1] - lst[0]
print(avrg)
print(mid)
print(frequen)
print(cvrg)
