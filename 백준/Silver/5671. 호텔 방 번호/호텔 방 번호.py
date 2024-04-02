while True :
    try:
        N, M = map(int, input().split())
    except:
        break
    result = 0
    for i in range(N, M+1):
        t = True
        a = set()
        for s in str(i):
            if s in a:
                t = False
                break
            else :
                a.add(s)
        if t == True:
            result += 1
    print(result)