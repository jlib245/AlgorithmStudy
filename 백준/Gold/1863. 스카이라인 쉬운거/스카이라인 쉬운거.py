import sys
input = sys.stdin.readline

n = int(input())
stack = []
cnt = 0
for i in range(n):
    x, y = map(int, input().split())
    if not stack and y != 0:
        stack.append(y)
        cnt += 1
    else :
        if y == 0 :
            while stack :
                stack.pop()
        elif stack[-1] < y :
            stack.append(y)
            cnt += 1
        else :
            while stack and stack[-1] > y :
                stack.pop()
            if stack and stack[-1] < y or not stack:
                stack.append(y)
                cnt += 1
print(cnt)