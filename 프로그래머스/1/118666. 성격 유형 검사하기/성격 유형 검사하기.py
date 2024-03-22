def solution(survey, choices):
    character = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    # 점수 계산
    for i in range(len(survey)):
        nonAgree = survey[i][0] 
        agree = survey[i][1]
        if choices[i] < 4 :
            character[nonAgree] += 4 - choices[i]
        elif choices[i] > 4 :
            character[agree] += choices[i] - 4
   # 성격 결론 도출
    answer = ""
    if character['R'] < character['T']:
        answer += 'T'
    else:
        answer += 'R'
    
    if character['C'] < character['F']:
        answer += 'F'
    else:
        answer += 'C'
    if character['J'] < character['M']:
        answer += 'M'
    else:
        answer += 'J'
    if character['A'] < character['N']:
        answer += 'N'
    else:
        answer += 'A'
        
        
            
                   
                   
    return answer