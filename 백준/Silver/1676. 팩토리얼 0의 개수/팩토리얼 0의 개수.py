inp = int(input())
num = 1
for i in range(1, inp+1):
    num *= i
num = str(num)[::-1]
n = 0
for i in num:
    if i == '0':
        n += 1
    else:
        break
print(n)