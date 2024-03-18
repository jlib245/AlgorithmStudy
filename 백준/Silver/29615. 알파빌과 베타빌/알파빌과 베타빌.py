N, M  =  map(int, input().split())
N_list = list(map(int, input().split()))
M_list = list(map(int, input().split()))
number = 0
for i in N_list[0:M]:
    if i in M_list:
        number += 1
print(M-number)