def f(n):
    lst = []
    a = n
    for i in range(8):
        b = a // 2
        c = a % 2
        lst.append(c)
        a = b
    res = []
    for i in range(8):
        if lst[i] == 1:
            res.append(i)
    return res        

N = int(input())
lst = list(map(int, input().split()))
K = int(input())

st = []

lst
for i in lst:
    l = f(i)
    if len(l) == 2:
        a, b= l
        st.append({a,b})

for i in range(len(st)-1, -1, -1):
    if K in st[i]:
        st[i].discard(K)
        K = st[i].pop()

print(K)