#!/usr/bin/python3
import sys

def TestingBlock(n):
    fourBit = [bin(x)[2:].zfill(4) for x in range(16)]
    b = [''.join(map(lambda x : fourBit[x][y], range(16))) for y in range(4)]
    d, r = divmod(n, 16)
    tb = [''.join(map(lambda x : b[y], range(d))) + b[y][0:r] for y in range(4)]
    return tb
def HeadNumber(n):
    return [''.join([str(x).zfill(4)[y] for x in range(n)]) for y in range(4)] 

T = int(input())
for t in range(1, T + 1):
    N, B , F = [int(x) for x in input().split(" ")]
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
            if not all(tb[j][i] == ds[j][i] for j in range(4)):
                if i < N-2:    
                    bad_set.add(i)
                    for y in range(4):
                        ds[y] = ds[y][0:i]+' '+ds[y][i:] 
                    j = i+1
                    break
        if i == len(ds[0])-1:
            i += 1
            while (i < N):     
                bad_set.add(i)
                i += 1

    print(' '.join([str(x) for x in sorted(list(bad_set))]))
    sys.stdout.flush()
    verdict = int(input())
    if verdict == -1:
        offset = N - 180
        for y in range(4):
            print(tb[y][offset:offset+180], file=sys.stderr)    
        print(N, B, F, file=sys.stderr)
        for y in range(4):
            print(ds[y][offset:offset+180], file=sys.stderr)    
        print(' ', file=sys.stderr)
        hn = HeadNumber(N)
        for y in range(4):
            print(hn[y][offset:offset+180], file=sys.stderr)
        print(' ', file=sys.stderr)    
        print(sorted(list(bad_set)), file=sys.stderr)
        sys.exit(t)
sys.exit(0)        
