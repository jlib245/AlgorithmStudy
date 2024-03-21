def solution(wallpaper):
    fileList = []
    #파일 위치 리스트 안에 넣기
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[x])):
            if wallpaper[x][y] == '#':
                fileList.append((x, y))
    #최소 범위 구하기
    answer = []
    i = fileList[0] 
    answer = [i[0],i[1],i[0],i[1]]
    for i in fileList:
            if i[0] < answer[0]:
                answer[0] = i[0]
            elif i[0] > answer[2]:
                answer[2] = i[0]
            if i[1] < answer[1]:
                answer[1] = i[1]
            elif i[1] > answer[3]:
                answer[3] = i[1]
    answer[2] = answer[2]+1
    answer[3] = answer[3]+1
    return answer