def poow(A, B, C):
    if B == 1:
        return A%C
    
    b = poow(A, B//2, C) % C
    
    if B % 2 == 1:
        return (b * b * A%C) % C
    else:
        return (b * b) % C

A, B, C = map(int, input().split())

print(poow(A, B, C))