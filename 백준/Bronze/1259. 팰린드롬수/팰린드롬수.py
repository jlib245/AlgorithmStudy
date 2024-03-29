while 1 :
    a = input()
    if a == '0':
        break
    dup = 0
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            dup += 1
    if dup > 0:
        print("no")
    else:
        print("yes")