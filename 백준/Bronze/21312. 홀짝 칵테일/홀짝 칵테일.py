def f(n):
    if n % 2 == 1:
        a = 0
    else:
        a = 1
    return (a, -n)

A, B, C = map(int, input().split())

cocktail = [A, B, C, A*B, B*C, C*A, A*B*C]
cocktail.sort(key=f)

print(cocktail[0])