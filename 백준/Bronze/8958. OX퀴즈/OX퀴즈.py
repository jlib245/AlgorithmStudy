N = int(input())
lst = []
for i in range(N):
    lst.append(input())
    
for i in range(N):
    score = 0
    combo = 0
    for s in lst[i]:
        if s == 'O':
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)