N = int(input())

dic = dict()
max_ = 0
for i in range(N):
    s = input()
    if not s in dic:
        dic[s] = 1
    else:
        dic[s] += 1
    if max_ < dic[s]:
        max_ = dic[s]
        set_ = set([s])
    elif max_ == dic[s]:
        set_.add(s)
lst = sorted(list(set_))
print(lst[0])
