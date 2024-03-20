def solution(today, terms, privacies):
    #약관 정리
    termDic = {}
    for i in range(len(terms)):
        termName, termMonth  = terms[i].split()
        termDic[termName] = int(termMonth)
    # 정보 나누기
    privacyList = []
    for i in range(len(privacies)):
        date, termterm = privacies[i].split()
        privacyList.append([list(map(int, date.split('.'))), termterm]) 
        
    # today 나누기
    todayDate = list(map(int, today.split('.')))
    # 약관 계산
    xStart = []
    for termStart in privacyList:
        YYYY = termStart[0][0]
        MM = termStart[0][1]
        DD = termStart[0][2]
        termMonth = termDic[termStart[1]]
        xYYYY = YYYY
        xMM = MM
        xDD = DD
        if MM + termMonth > 12:
            xYYYY = YYYY + (MM + termMonth) // 12
            xMM = (MM + termMonth) % 12
        else:
            xMM = MM + termMonth
        xStart.append([xYYYY, xMM, xDD])
    #비교해보기
    xList = []
    for i in range(len(xStart)):
        xDate = xStart[i]
        
        if dateCompare(todayDate,xDate)== 1:
            xList.append(i+1)
    return xList
def dateCompare(today, X):
    todayDay = today[2]+ (today[1] + (today[0] * 12)) * 28 
    xDay = X[2]+ (X[1] + (X[0] * 12)) * 28
    if xDay <= todayDay:
        return 1
    else:
        return 0
    