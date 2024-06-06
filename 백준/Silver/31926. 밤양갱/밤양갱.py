"""
1. d
2. da
3. dal
4. dald
5. daldi   
6. daldidal     #dal 복붙 
7. daldidalg
8. daldidalgo

+daldidan
1. daldida
2. daldidan

N = 1일 때
8 + 2 = 10
N = 2일 때
8 + 1 + 2  = 11

N = 4일 때
daldidalgo = 8
daldidalgodaldidalgo = 9
daldidalgodaldidalgodaldidalgodaldidalgo = 10
daldidalgodaldidalgodaldidalgodaldidalgodaldidan = 12

N = 7일 때
daldidalgo = 8
daldidalgodaldidalgo = 9
daldidalgodaldidalgodaldidalgodaldidalgo = 10
daldidalgodaldidalgodaldidalgodaldidalgodaldidalgodaldidalgodaldidalgodaldida = 11 #daldidalgo * 3 + daldida 복붙
daldidalgodaldidalgodaldidalgodaldidalgodaldidalgodaldidalgodaldidalgodaldidan = 12

결론 
if N != 2**k (k는 임의의 자연수)
res(N) = 8 + int(log2(N)) + 2
if N == 2**k
res(N) = 8 + int(log2(N)) + 2

-> N이 2**k일 때랑 아닐 때랑 똑같음
"""

import math
N = int(input())

res = int(math.log2(N)) + 10

print(res)