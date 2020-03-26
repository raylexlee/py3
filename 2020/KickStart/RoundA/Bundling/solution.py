def prefixOf(a, b):
    px = ''
    for x in range(min(len(a),len(b))+1):
        if a.startswith(b[0:x]):
            px = b[0:x]
        else:
            break
    return px        
T = int(input())
for i in range(1, T + 1):
    N, K = [int(s) for s in input().split(" ")]
    w = sorted([input() for j in range(N)], reverse=True)
    p = [prefixOf(w[0], w[1])]
    for j in range(1, N-1):
        upper = prefixOf(w[j-1], w[j])
        lower = prefixOf(w[j+1], w[j])
        if upper and lower:
            if len(upper) > len(lower):
                p.append(upper)
            else:
                p.append(lower)
            continue
        if upper:
            p.append(upper)
            continue
        if lower:
            p.append(lower)
            continue
        p.append('')        
    p.append(prefixOf(w[N-2],w[N-1]))
    c = {}
    for x in p:
        if not x:
            continue
        if x in c:
            c[x] += 1
        else:
            c[x] = 1        
    m = 0
    while (len(c)):
        mlk = max(len(k) for k in c)
        for k, v in c.items():
            if len(k) == mlk:
                break
        d, r = divmod(v, K)
        m += d * mlk
        c.pop(k)
        if r == 0:
            continue
        j = mlk-1
        while j:
            if k[0:j] in c:
                c[k[0:j]] += r
                break
            j -= 1
    print("Case #{}: {}".format(i, m))