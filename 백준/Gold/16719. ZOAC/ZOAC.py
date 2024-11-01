ZOAC = input()
ans = []
TF = [False]*len(ZOAC)
def fres():
    res = ""
    for i in range(len(ZOAC)):
        if TF[i]:
            res += ZOAC[i]
    print(res)
    return

def f(s : int, e : int, c : int, res = "") -> None :
    if s == e :
        TF[s] = True
        fres()
        return 
    firstIdx = -1
    firstVal = 'a'
    for i in range(s, e+1):
        if firstVal > ZOAC[i] :
            firstVal = ZOAC[i]
            firstIdx = i
    TF[firstIdx] = True
    fres()
    if firstIdx != e :
        f(firstIdx+1, e, 1, res)
    if firstIdx != s :
        f(s, firstIdx-1, 0, res)
    return 

f(0, len(ZOAC)-1, 1)
