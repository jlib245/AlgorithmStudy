def solution(nums):
    thousand = [0]*3001
    thousand[0] = 1
    thousand[1] = 1
    
    for i in range(2, 3001):
        if thousand[i] == 0:
            to1 = 2*i
            while to1 < 3000:
                thousand[to1] = 1
                to1 += i
    numnum = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                a = nums[i]+nums[j]+nums[k]
                if thousand[a] == 0:
                    numnum+=1
        
    return numnum