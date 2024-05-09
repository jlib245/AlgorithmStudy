def f(s, start, end):
    Pal = True
    i = 0
    for i in range(len(s)//2-start+1):
        a, b = s[start+i], s[end-i]
        if s[start + i] != s[end-i]:
            Pal = False
            break
    return (Pal, i)

T = int(input())
for _ in range(T):
    s = input()
    Pal, i1 = f(s, 0, len(s)-1)
    if Pal:
        print(0)
        continue
    Pal, i = f(s, i1+1, len(s)-i1-1)
    if Pal:
        print(1)
        continue
    Pal, i = f(s, i1, len(s)-i1-2)
    if Pal:
        print(1)
    else:
        print(2)           