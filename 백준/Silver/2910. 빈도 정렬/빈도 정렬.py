N, C = map(int, input().split())

def f(num):
    a,b = dic[num]
    return (-a, b)

arr = list(map(int, input().split()))

dic = dict()
order = 0
for i in arr:
    if i not in dic.keys():
        dic[i] = [0,order]
        order += 1
    else:
        dic[i][0] += 1

arr.sort(key=f)

print(*arr)