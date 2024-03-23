def solution(n):
    result = []
    return hanoi(n, 1, 2, 3, result)

def hanoi(n, start, mid, end, result = list()):
    if n == 1:  
        result = [[start, end]]
        return result
    else :
        a = hanoi(n-1, start, end, mid, result)
        m = [[start, end]]
        b = hanoi(n-1, mid, start, end, result)
        result = a+m+b
        return result
        
    