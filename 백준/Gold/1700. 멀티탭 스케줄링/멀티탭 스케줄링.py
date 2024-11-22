from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

use = list(map(int, input().split()))
dic = defaultdict(list)

for i in range(K) :
    dic[use[i]].append(i)

using = set()
cnt = 0
for i in range(len(use)) :
    x = use[i]
    if len(using) < N :
        using.add(x)
    elif x in using :
        continue
    else :
        the_last_x = -1
        the_last_idx = -1
        for rx in using :
            for j in dic[rx] :
                if i < j :
                    if the_last_idx < j :
                        the_last_idx = j
                        the_last_x = rx
                    break
            else :
                the_last_x = rx
                break
        cnt += 1
        using.discard(the_last_x)
        using.add(x)
print(cnt)