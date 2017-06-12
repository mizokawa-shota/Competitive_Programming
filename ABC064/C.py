N = int(input())
a = list(map(int, input().split()))

d = [0] * 9
for i in a:
    if i <= 399:
        d[0] = 1
    elif i <= 799:
        d[1] = 1
    elif i <= 1199:
        d[2] = 1
    elif i <= 1599:
        d[3] = 1
    elif i <= 1999:
        d[4] = 1
    elif i <= 2399:
        d[5] = 1
    elif i <= 2799:
        d[6] = 1
    elif i <= 3199:
        d[7] = 1
    else:
        d[8] += 1

minimam = max(1, sum(d[:8]))
maximam = sum(d)

print(minimam, maximam)
