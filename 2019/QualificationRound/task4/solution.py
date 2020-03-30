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
    N, B , F = [int(x) for x in input().split(" ")]
    tb = TestingBlock(N)
    ds = []

    for y in range(4): 
        print(tb[y])
        sys.stdout.flush()
        ds.append(input())

    ztb = zip(*tb)
    zds = zip(*ds)
    bad_set = []
    d_col = next(zds, None)
    for j, t_col in enumerate(ztb):
        if t_col == d_col:
            d_col = next(zds, None)
        else:
            bad_set.append(j)
    print(*bad_set)            
    sys.stdout.flush()
    verdict = int(input())
    if verdict == -1:
        sys.exit(t)
sys.exit(0)        
