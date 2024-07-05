def f(n):
    if n == 0:
        return '-'
    res = ""
    divs = f(n-1)
    res += divs
    res += ' '*(3**(n-1))
    res += divs
    return res

while 1:
    try:
        N = int(input())
        print(f(N))
    except :
        break