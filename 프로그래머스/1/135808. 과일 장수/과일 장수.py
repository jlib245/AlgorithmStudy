def solution(k, m, score):
    score.sort()
    total = 0
    for i in range(len(score)//m):
        for j in range(m):
            s = score.pop()
        total += s * m        
    
    return total