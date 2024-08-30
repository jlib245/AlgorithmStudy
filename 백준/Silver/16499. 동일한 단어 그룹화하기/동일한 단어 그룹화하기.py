N = int(input())
group = set()
cnt = 0
for i in range(N):
    lst = input()
    capital = [0]*26
    for c in lst :
        capital[ord(c)-97] += 1
    tc = tuple(capital)
    if not tc in group :
        group.add(tc)
        cnt += 1
print(cnt)