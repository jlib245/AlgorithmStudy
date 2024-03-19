def solution(cards):
    BoxBox = []
    CheckBox = []
    for i in range(len(cards)):
        oneRound = []
        this = cards[i]
        while this not in CheckBox :
            oneRound.append(this)
            CheckBox.append(this)
            this = cards[this-1]
        BoxBox.append(len(oneRound))
    BoxBox.sort(reverse = True)
    answer = BoxBox[0] * BoxBox[1]
            
        
    return answer