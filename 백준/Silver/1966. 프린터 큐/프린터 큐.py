for i in range(int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    q = []
    for i in range(N):
        q.append((lst[i], i))
    sorQ = lst[::]
    sorQ.sort(reverse=True)
    t = 0
    while q != []:
        if sorQ[0] == q[0][0]:
            t += 1
            sorQ.pop(0)
            a = q.pop(0)
            if a[1] == M:
                print(t)
                break
        else:
            q.append(q.pop(0))