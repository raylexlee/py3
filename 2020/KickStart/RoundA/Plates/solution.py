T = int(input())
for i in range(1, T + 1):
    N, K, P = [int(s) for s in input().split(" ")]
    plate = [[int(s) for s in input().split(" ")] for j in range(N)]
    for j in range(N):
        for k in range(1, K):
            plate[j][k] += plate[j][k-1]    
            
    print("Case #{}: {}".format(i, max))    