N = int(input())

result = 0
previous = -1
for _ in range(N):
    s = input()
    set_ = set()
    group = True
    
    for i in s:
        if i not in set_ or i == previous:
            set_.add(i)
        else:
            group = False
        previous = i    

    if group == True:
        result += 1
        
print(result)