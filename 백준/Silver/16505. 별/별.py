def star(n):
    if n == 0 :
        return ['*']
    prev = star(n-1)
    lst = []
    for i in range(2**(n-1)) :
        blank = ' ' * i
        lst.append(blank.join([prev[i], prev[i]]))
    for row in prev :
        lst.append(row)
    return lst

N = int(input())

ans = star(N)
print(*ans, sep='\n')