S = input("")
divide = S.split("+")
total = (len(divide)-1)*0.5
number = 0
for i in divide:
    for j in i:
        number += 1
        if j == 'A':
            total += 4
        elif j == 'B':
            total += 3
        elif j == 'C':
            total += 2
        elif j == 'D' :
            total += 1
print(total/number)