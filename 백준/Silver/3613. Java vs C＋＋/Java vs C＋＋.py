s = input()
res = ''
B = False
error = [0, 0]
for i in range(len(s)):
    if s[i] == '_':
        if B or i == 0:
            print("Error!")
            exit()
        B = True
        error[0] = 1
    elif 65 <= ord(s[i]) <= 90:
        if i == 0:
            print("Error!")
            exit()
        res += '_' + chr(ord(s[i]) + 32)
        error[1] = 1
    elif B :
        res += chr(ord(s[i]) - 32)
        B = False
    else:
        res += s[i]
if error[0] and error[1] or B:
    print("Error!")
else:
    print(res)