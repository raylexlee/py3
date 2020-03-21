#!/usr/bin/python3
import sys

def TestingBlock(n):
    fourBit = [bin(x)[2:].zfill(4) for x in range(16)]
    b = [''.join(map(lambda x : fourBit[x][y], range(16))) for y in range(4)]
    d, r = divmod(n, 16)
    tb = [''.join(map(lambda x : b[y], range(d))) + b[y][0:r] for y in range(4)]
    return tb

T = int(input())
for t in range(1, T + 1):
    N, B, F = [int(x) for x in input().split(" ")]
    tb = TestingBlock(N)
    ds = []

    for y in range(4): 
        print(tb[y])
        sys.stdout.flush()
        ds.append(input())

    bad_set = set()
    j = 0
    while (len(bad_set) < B): 
        for i in range(j, len(ds[0])):
            if not all(tb[j][x] == ds[j][x] for j in range(4)):
                if i < N-2:    
                    bad_set.add(i)
                    for y in range(4):
                        ds[y] = ds[y][0:i]+tb[y][i]+ds[y][i:] 
                    j = i+1
                    break
                else:
                    bad_set.add(N-1)

    print("Case #{}: {}".format(t, ' '.join(sorted(list(bad_set)))))
    sys.stdout.flush()