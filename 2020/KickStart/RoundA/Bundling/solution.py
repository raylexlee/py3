T = int(input())
for i in range(1, T + 1):
    N, K = [int(s) for s in input().split(" ")]
    w = sorted([input() for j in range(N)])
    g = divmod(N, K)[0]
    max_sum = 0
    for j in range(g):
        b = w[j*K:j*K+K]
        max = 0
        for x in range(1,len(b[0])+1):
            if not all(b[k].startswith(b[0][0:x]) for k in range(1,K)):
                break
            max = x
        max_sum += max
    print("Case #{}: {}".format(i, max_sum))