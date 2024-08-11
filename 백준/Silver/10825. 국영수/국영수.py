import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
lst = []
for _ in range(N):
    name, Korean, English, Math = input().split()
    Korean, English, Math = int(Korean), int(English), int(Math)
    lst.append((name, Korean, English, Math))
lst.sort(key= lambda x : (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(lst[i][0])