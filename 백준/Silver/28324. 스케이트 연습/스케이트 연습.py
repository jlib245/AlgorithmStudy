N = int(input())
course = list(map(int,input().split())) + [0]
sum_ = 0
for i in range(N-1, -1, -1):
    limitByThis = course[i]
    limitByAfter = course[i+1]+1
    course[i] = min(limitByThis, limitByAfter)
    sum_ += course[i]
print(sum_)