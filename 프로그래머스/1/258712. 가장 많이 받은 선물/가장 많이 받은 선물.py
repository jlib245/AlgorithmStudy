def solution(friends, gifts):
    lenFriends = len(friends)
    expect = [0]*len(friends)
    giftScore = []
    giftTable = [[0]*lenFriends for i in range(lenFriends)]
    friendsNumber = {}
    # friends 리스트랑 넘버 뒤집어 놨는데 이게 맞을지..??
    for i in range(lenFriends):
        friendsNumber[friends[i]] = i
    # 선물 준 것을 왼쪽 표로 나타낸 것.
    for i in gifts:
        transGift = i.split()
        giftTable[friendsNumber[transGift[0]]][friendsNumber[transGift[1]]] += 1
    # 선물 지수 계산 및 입력.
    for i in range(lenFriends):
        sendScore = 0
        receiveScore = 0
        for j in range(lenFriends):
            sendScore += giftTable[i][j]
        for j in range(lenFriends):
            receiveScore += giftTable[j][i]
        giftScore.append(sendScore - receiveScore)
    # 다음 달 예상하기
    for i in range(lenFriends):
        for j in range(lenFriends):
            if i != j:
                sendRecord = giftTable[i][j]
                receiveRecord = giftTable[j][i]
                if sendRecord < receiveRecord:
                    expect[j] += 1
                elif sendRecord == receiveRecord and giftScore[i] < giftScore[j]:
                    expect[j] += 1
    # 많이 받을 사람 체크
    answer = max(expect)
    return answer
