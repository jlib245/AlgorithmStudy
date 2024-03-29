lst = []
def back():
    if len(lst) == M:
        for i in lst:
            print(i, end= ' ')
        print('')
        return
    for i in number:
        if not i in lst:
            lst.append(i)
            back()
            lst.pop()
        
N, M = map(int,input().split())
number = list(map(int,input().split()))
number.sort()
back()