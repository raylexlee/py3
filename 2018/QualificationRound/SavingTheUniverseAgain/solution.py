T = int(input())
for x in range(1, T+1):
    Dstr, P = input().split()
    D = int(Dstr)
    N = len(P)
    c = []
    for i in range(N):
        if P[i] == 'C':
            c.append(i)
    cL = len(c)
    if cL == 0:
        y = '0' if N <= D else 'IMPOSSIBLE'
        print("Case #{}: {}".format(x, y))
        continue
    c.append(N)
    a = c[0] +sum([(1 << (i+1))*(c[i+1]-c[i]-1) for i in range(cL)])
    if a <= D:
        print("Case #{}: 0".format(x))
        continue
    y = 0
    j = cL - 1
    while ((a > D) and (c[0] < N-cL)):
        while ((j > 0) and (c[j+1] - c[j] == 1)):
            j -= 1
        c[j] += 1
        y += 1
        a -= 1 << j
    if a <= D:
        print("Case #{}: {}".format(x, y))
    else:    
        print("Case #{}: IMPOSSIBLE".format(x))