import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = dict()
for _ in range(N):
    site, pw = input().rstrip().split()
    dic[site] = pw
for _ in range(M):
    print(dic[input().rstrip()])