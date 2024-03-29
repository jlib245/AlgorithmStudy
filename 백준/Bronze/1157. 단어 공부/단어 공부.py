a = list(input().upper())
lst = [0]*91
for i in a:
    lst[ord(i)] += 1
# mx[0] = 값, [1] = 인덱스, [2] = 중복 여부
mx = [0,0,0]
for i in range(65, 91):
    b = lst[i]
    if b > mx[0]:
        mx[0] = b
        mx[1] = i
        mx[2] = 0
    elif b == mx[0]:
        mx[2] += 1
if mx[2] > 0:
    print('?')
else:
    print(chr(mx[1]))