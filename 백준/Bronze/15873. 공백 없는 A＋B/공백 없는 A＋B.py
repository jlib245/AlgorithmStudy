s = input()
if len(s) == 2:
    print(int(s[0])+int(s[1]))
elif len(s) == 3:
    ns = s.replace('10', '')
    print(int(ns)+10)
else:
    print(20)