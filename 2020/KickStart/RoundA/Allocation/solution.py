T = int(input())
for i in range(1, T+1):
    N, B = [int(s) for s in input().split(" ")]
    cost = sorted([int(s) for s in input().split(" ")])
    sum = 0
    prev_sum = sum
    max = N
    for j in range(N):
        prev_sum = sum
        sum += cost[j]
        if sum > B:
            max = j
            break
        if sum == B:
            max = j + 1
            break
    print("Case #{}: {}".format(i, max))