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
        print(xDate, todayDate)
        if xDate[0] < todayDate[0]:
            xList.append(i+1)
        elif xDate[0] == todayDate[0] and xDate[1] < todayDate[1]:
            xList.append(i+1)
        elif xDate[0] == todayDate[0] and xDate[1] == todayDate[1] and xDate[2] <= todayDate[2]:
            xList.append(i+1)
    return xList