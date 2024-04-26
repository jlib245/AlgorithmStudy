X = int(input())

i = 1
cnt = 0
while 1:
    cnt += i
    if cnt >= X:
        break
    i += 1

cha = cnt - X 
if i % 2 == 0:
    print(f"{i-cha}/{cha + 1}")
else:
    print(f"{cha+1}/{i-cha}")