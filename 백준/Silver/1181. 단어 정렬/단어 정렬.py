import sys
def f(a):
    r = [0]*2
    r[0] = len(a)
    r[1] = a
    return r
l = []
for i in range(int(input())):
    l.append(sys.stdin.readline().rstrip())
l = list(set(l))
l.sort(key= f)
for i in l:
    print(i)