from random import seed
from random import randint
from random import sample
seed(1)
N = randint(80,90)
B = randint(1, 15)
__bad_set = set(sample(range(N), B))
def _answer_query(N,  bitstring):
    answer = ""
    for i in range(N):
        if i not in __bad_set:
            answer += bitstring[i]
    return answer
def TestingBlock(n):
    b = ''.join(map(lambda x : bin(x)[2:], range(8)))
    d, r = divmod(n, len(b))
    tb = ''.join(map(lambda x : b, range(d)))
    tb += b[0:r]    
    return tb

tb = TestingBlock(N)
distort  = _answer_query(N, original)
ds = distort
bb = len(tb) - len(distort)
bad_list = []
j = 0
while (len(bad_list) < bb): 
    for i in range(j, len(ds)):
        if tb[i] != ds[i]:
            if i < N-2:    
                bad_list.append(i)
                ds = ds[0:i]+tb[i]+ds[i:]
                j = i+1
                break
            else:
                bad_list.append(N-1)


        

#print(original)
#print(distort)