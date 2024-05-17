def f(s):
    stack = []
    res = ''
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')' :
            while stack:
                a = stack.pop()
                if a == '(':
                    break
                else:
                    res += a
        elif not c in prior:
            res += c
        else:
            if stack and not prior[c] > prior[stack[-1]]:
                while stack:
                    a = stack.pop()
                    if a == '(' or prior[c] > prior[a]:
                        stack.append(a)
                        break
                    else:
                        res += a
            stack.append(c)  
    while stack:
        res += stack.pop()
    return res

s = input()
prior = {'+' : 0,'-' : 0,'*' : 1, '/' : 1, '(':2}
res = f(s)
print(res)