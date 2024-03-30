S = list(input())
for i in range(0, 26):
    char = chr(i+97)
    if char in S:
        print(S.index(char))
    else:
        print(-1)