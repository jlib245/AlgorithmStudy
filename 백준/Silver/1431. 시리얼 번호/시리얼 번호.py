# 버블 정렬 한 줄
def serialComPare(now = int(), next = int(), nLine= int()):
    if now == nLine -1:
        return
    else:    
        serialNow = serialList[now]
        serialNext = serialList[next]
        # 1. A, B의 길이가 다르면 짧은 것이 먼저 온다.
        if len(serialNow) < len(serialNext):
            pass
        elif len(serialNow) > len(serialNext):
            serialList[now] = serialNext
            serialList[next] = serialNow
        else :
            # 2. 만약 서로의 길이가 같다면, 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저 온다.(숫자만)
            sumNow = 0
            sumNext = 0
            for i in serialNow:
                try:
                    number = int(i)
                    sumNow += number
                except:
                    pass
            for i in serialNext:
                try:
                    number = int(i)
                    sumNext += number
                except:
                    pass
            if sumNow < sumNext:
                pass
            elif sumNow > sumNext:
                serialList[now] = serialNext
                serialList[next] = serialNow
            else:
                # 3. 1,2번 둘 다 같다면, 사전순으로 비교한다. 숫자가 알파벳보다 사전 순으로 작다.
                for i in range(len(serialNow)):
                    try :
                        dicNow = int(serialNow[i])
                    except :
                        dicNow = ord(serialNow[i])
                    try : 
                        dicNext = int(serialNext[i])
                    except :
                        dicNext = ord(serialNext[i])
                    if dicNow < dicNext:
                        break
                    elif dicNow > dicNext:
                        serialList[now] = serialNext
                        serialList[next] = serialNow
                        break
                    else:
                        pass
        serialComPare(next, next+1, nLine)
# 시리얼 수 입력
nLine = int(input())
# 시리얼 번호 입력
serialList = []
for i in range(nLine):
    serialList.append(input())
# 버블정렬 시작
for i in range(nLine):
    serialComPare(0, 1, nLine)
# 프린트
for i in serialList:
    print(i)