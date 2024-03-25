def solution(n):
    triangle = [[0]*i for i in range(1, n+1) ]
    line = 0
    number = 0
    for i in range(n, 0, -1):
        line += 1
        lineAngle = line % 3
        lineAngleNum = line // 3 +1
        if lineAngle == 1:
            for j in range(i):
                number += 1
                triangle[lineAngleNum * 2-2+j][lineAngleNum-1] = number
        elif lineAngle == 2:
            for j in range(i):
                number += 1
                triangle[n-lineAngleNum][lineAngleNum + j] = number
        else :
            for j in range(i):
                number += 1
                triangle[n-lineAngleNum-j][n-lineAngleNum*2+2-j] = number
    answer = []
    for i in triangle:
        answer = answer + i
    return answer