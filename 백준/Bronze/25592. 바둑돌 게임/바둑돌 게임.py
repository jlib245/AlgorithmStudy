N = int(input())
i = 1
while (i - N) <= 0:
    N -= i
    i += 1
if i % 2 == 1:
    print(i-N)
else:
    print(0)