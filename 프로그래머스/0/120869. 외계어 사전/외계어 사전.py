def solution(spell, dic):
    for word in dic:
        a = 0
        for spelling in spell:
            if spelling in word:
                a += 1
        if a == len(spell):
            return 1
    
    return 2
    
        
    
                
    return answer