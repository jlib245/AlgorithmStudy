S = int(input())
cnt = 0
hap = 0
while hap < S:
    cnt += 1
    hap += cnt
if hap == S:
    print(cnt)
else:
    print(cnt-1)