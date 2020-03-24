T = int(input())
for i in range(1, T + 1):
    N, K, P = [int(s) for s in input().split(" ")]
    a = []
    w = []
    for j in range(N):
        ps = [int(s) for s in input().split(" ")]
        for k in range(1, K):
            ps[k] += ps[k-1]    
        if P > K:
            for k in range(K, P):
                ps.append(None)        
        if j == 0:
            w = ps.copy()
            a = w.copy()
            continue
        for l in range(P):
            if l == 0:
                a[0] = max(w[0], ps[0])
                continue
            if ps[l] is not None:
                a[l] = max(ps[l], w[l])
            for k in range(l):
                if a[l] is None:
                    a[l] = w[k] + ps[l-1-k]
                else:    
                    a[l] = max(a[l], w[k] + ps[l-1-k])
        w = a.copy()        
    print("Case #{}: {}".format(i, w[P-1]))    