N = int(input())

lst = []
while N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            N = N // i
            lst.append(i)
            break
        
for i in lst:
    print(i)