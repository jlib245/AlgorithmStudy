s = input()

lst = [0]*26
for i in s:
    lst[ord(i)-65] += 1

cnt = 0
check = -1
for i in range(26):
    if lst[i] % 2 == 1:
        cnt += 1
        check = i
        
if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    for i in range(26):
        c = chr(i+65)
        if i != check or lst[i] != 1:
            for _ in range(lst[i]//2):
                print(c, end='')
    if check != -1:
        print(chr(check+65), end='')
    for i in range(25, -1, -1):
        c = chr(i+65)
        if i != check or lst[i] != 1:
            for _ in range(lst[i]//2):
                print(c, end='')