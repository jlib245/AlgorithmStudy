N = int(input())
s = input()
red = 0
blue = 0
previous = 0
for i in s:
    if i == previous:
        continue
    if i == 'R':
        red += 1
    else :
        blue += 1
    previous = i
if blue > red:
    print(red+1)
else:
    print(blue+1)