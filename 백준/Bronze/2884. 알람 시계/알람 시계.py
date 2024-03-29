H, M = map(int, input().split())
T = H * 60 + M - 45
if T < 0:
    T += 1440
print(T//60, T%60)