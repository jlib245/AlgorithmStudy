lst = []
leng = []
mx_len = 0

for i in range(5):
    s = input()
    lst.append(s)

    leng.append(len(s))
    if mx_len < len(s):
        mx_len = len(s)

for j in range(mx_len):
    for i in range(5):
        if j < leng[i]:
            print(lst[i][j], end='')