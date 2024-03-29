lst = list(map(int,input().split()))
for i in range(5):
    lst[i] *= lst[i]
print(sum(lst)%10)