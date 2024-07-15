'''
1       1   1

10      1   2
11      2

100     1   5
101     2
110     2
111     3

1000    1   13
1001    2
1010    2
1011    3
1100    2
1101    3
1110    3
1111    4

dp[i] = (2**i - 1) 까지의 모든 합
lst[i] = i번째 인덱스까지의 모든 합
'''
def f(N : int):
    lenN = N.bit_length()
    binN = bin(N)
    res = 0
    cnt = 0
    for i in range(lenN-1, -1, -1):
        if int(binN[-i-1]):
            res += lst[i] + (2**i)*cnt  
            cnt += 1
    return res
    
            
A, B = map(int, input().split())
lenB = B.bit_length()
dp = [0]*(lenB+1)
dp[1] = 1
for i in range(2, lenB+1):
    dp[i] = 1 + 2* dp[i-1] + (2**(i-1)-1)
lst = [0]*(lenB)
for i in range(lenB):
    lst[i] = dp[i] + 1
ans = f(B) - f(A-1)
print(ans)