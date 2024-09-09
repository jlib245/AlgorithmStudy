import sys
input = lambda : sys.stdin.readline()

while 1 : 
    s = input().replace('\n', '')
    if s == "***" :
        break
    print(s[::-1])