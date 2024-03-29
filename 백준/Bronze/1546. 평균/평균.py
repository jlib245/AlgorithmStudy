N = int(input())
G = list(map(int, input().split()))
print(sum(G)/N/max(G)*100)
