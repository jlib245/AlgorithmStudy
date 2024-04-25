N = int(input())

for i in range(1, N+1):
    if i == 1:
        print(' '*(N-i) + '*')
    elif i != N:
        print(' '*(N-i)+'*'+' '*(2*i-3)+'*')
    else:
        print('*'*(2*N-1))