N = int(input())
M = int(input())
S = input()
cnt = 0
TF = False
res = 0
for i in range(1, M-1):
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        TF = True
        cnt += 1
        if cnt >= N:
            res += 1
    elif TF:
        TF = False
    elif cnt :
        cnt = 0
print(res)