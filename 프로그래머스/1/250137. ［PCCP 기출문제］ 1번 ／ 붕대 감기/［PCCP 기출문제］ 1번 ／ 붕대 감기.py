from collections import deque
def solution(bandage, health, attacks):
    attacks = deque(attacks)
    time = 1
    bt, x, y = bandage
    h = health
    while attacks:
        ht = 0
        a = attacks.popleft()
        while time != a[0]:  
            h += x
            ht += 1
            if ht == bt:
                ht = 0
                h += y
            if h > health:
                h = health
            time += 1
        h -= a[1]

        time += 1
        if h <= 0:
            return -1
    answer = h
    return answer