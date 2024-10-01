Y, M, D = map(int, input().split())
stY, stM, stD = map(int, input().split())

a = stY-Y
if stM > M :
    print(a)
elif stM == M :
    if stD >= D :
        print(a)
    else :
        print(a-1)
else :
    print(a-1) 
print(a+1)
print(a)