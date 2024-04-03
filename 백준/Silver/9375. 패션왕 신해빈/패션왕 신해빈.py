for _ in range(int(input())):
    n = int(input())
    dic = dict()
    for _ in range(n):
        wear, weartype = input().split()
        if weartype in dic:
            dic[weartype] += 1
        else :
            dic[weartype] = 1
    result = 1
    for i in list(dic.values()):
        result *= i+1
    result -= 1
    print(result)
