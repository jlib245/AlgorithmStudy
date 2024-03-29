for i in range(int(input())):
    t, s = input().split()
    t = int(t)
    for i in s:
        print(i*t, end='')
    print('')
        