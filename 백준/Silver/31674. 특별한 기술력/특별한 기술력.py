import sys
input = sys.stdin.readline

N = int(input())

H = list(map(int ,input().split()))
H.sort(reverse=True)

P = 10**9+7

result = 0
for i in range(N):
    result = ((result*2)%P + H[i]) % P

print(result)
