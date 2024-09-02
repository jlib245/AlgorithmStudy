N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

tshirts = 0
for x in size :
    tshirts += (x-1)//T+1
print(tshirts)
print(N//P, N % P)