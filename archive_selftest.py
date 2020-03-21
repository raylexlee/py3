from random import seed
from random import randint
from random import sample
seed(1)
N = randint(900,1024)
#N = 1022
F = 4
#B = randint(10,min(15, N-1))
B = 15
__bad_set = set(sample(range(N), B))
#__bad_set = set(range(879, 879+B))
def _answer_query(N,  bitstring):
    answer = ""
    for i in range(N):
        if i not in __bad_set:
            answer += bitstring[i]
    return answer
def HeadNumber(n):
    return [''.join([str(x).zfill(2)[y] for x in range(n)]) for y in [0,1]] 
        
def TestingBlock(n):
    fourBit = [bin(x)[2:].zfill(4) for x in range(16)]
    b = [''.join(map(lambda x : fourBit[x][y], range(16))) for y in range(4)]
    d, r = divmod(n, 16)
    tb = [''.join(map(lambda x : b[y], range(d))) + b[y][0:r] for y in range(4)]
    return tb

tb = TestingBlock(N)
ds = [_answer_query(N, tb[y]) for y in range(4)]
def columnsAreEqual(x):
    return all(tb[j][x] == ds[j][x] for j in range(4))

bb = len(tb[0]) - len(ds[0])
bad_set = set()
j = 0
while (len(bad_set) < bb): 
    for i in range(j, len(ds[0])):
        if not columnsAreEqual(i):
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

#for y in range(4):
#    print(tb[y])    
#print(' ')
#for y in range(4):
#    print(ds[y])    
#print(' ')
hn = HeadNumber(N)
#for y in range(2):
#    print(hn[y])
#print(' ')    
print(sorted(list(__bad_set)))
print(sorted(list(bad_set)))
