while 1:
    s = input()
    if s == "end":
        break
    gather = {'a', 'e', 'i','o','u'}
    
    acceptable = True
    gathercnt = 0
    for i in range(len(s)):
        if s[i] in gather:
            gathercnt += 1

        if i >= 2 and ((s[i] in gather and s[i-1] in gather and s[i-2] in gather)or(s[i] not in gather and s[i-1] not in gather and s[i-2] not in gather)):
            acceptable = False
            break
        elif i >= 1 and 'e' != s[i] == s[i-1] != 'o' :
            acceptable = False
            break

    if not gathercnt:
        acceptable = False

    if acceptable:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')