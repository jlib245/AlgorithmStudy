list1 = [1000000]*3000001
list1[1] = 0
X = int(input())
for i in range(1, X+1):
    if list1[i]+1 < list1[i*3]:
        list1[i*3] = list1[i]+1
    if list1[i]+1 < list1[i*2]:
        list1[i*2]= list1[i]+1
    if list1[i]+1 < list1[i+1]:
        list1[i+1]= list1[i]+1
print(list1[X])