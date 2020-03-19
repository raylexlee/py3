t = int(input())
for i in range(1, t+1):
    n, p = [int(x) for x in input().split(" ")]
    s = sorted([int(x) for x in input().split(" ")], reverse=True)
    ss = []
    for j in range(0, n-p+1):
        ss.append(sum(s[j : j+p]))
    m = min(map(lambda x : p * s[x] - ss[x], range(0, n-p+1)))
    print("Case #{}: {}".format(i, m))    