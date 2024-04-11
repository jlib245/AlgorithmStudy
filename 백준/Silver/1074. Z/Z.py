N, r, c = map(int, input().split())

def f(N, a , b):
    if N == 0:
        return 0
    
    if r < a + 2**(N-1):
        if c < b + 2**(N-1):
            result =  f(N-1, a, b)
            return result
        else:
            result =  f(N-1, a, b+2**(N-1))
            return (4**(N-1)) + result
    else:
        if c < b + 2**(N-1):
            result =  f(N-1, a+2**(N-1), b)
            return (4**(N-1))*2 + result
        else:
            result =  f(N-1, a+2**(N-1), b+2**(N-1))
            return (4**(N-1))*3 + result

print(f(N, 0, 0))