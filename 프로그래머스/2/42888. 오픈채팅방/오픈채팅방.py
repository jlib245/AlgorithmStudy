def solution(record):
    length = len(record)
    recordDic = {}
    
    for i in range(length):
        record[i] = record[i].split()
        if record[i][0] == "Enter":
            recordDic[record[i][1]] = record[i][2]
        elif record[i][0] == "Change":
            recordDic[record[i][1]] = record[i][2]
                                  
    result = []
    for i in range(length):
        if record[i][0] == "Enter":
            result.append(f"{recordDic[record[i][1]]}님이 들어왔습니다.")
        elif record[i][0] == "Leave":
            result.append(f"{recordDic[record[i][1]]}님이 나갔습니다.")
    return result