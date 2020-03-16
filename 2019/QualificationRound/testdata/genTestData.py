from random import seed
from random import randint
from random import sample
import os
dn = os.path.dirname(os.path.realpath(__file__))
seed(1)
primeList = []
pangramList = []
f = open(os.path.join(dn,"ascendingPrimes.txt"), "rt")
for x in f:
    primeList.append(int(x))
f.close()

f = open(os.path.join(dn,"qualifiedPangrams.txt"), "rt")
for x in f:
    pangramList.append(x.strip('\n'))
f.close()


f = open(os.path.join(dn,"answer100.txt"), "a")

primeListLength = len(primeList)
pangramListLength = len(pangramList)
# t = randint(30, 100)
t = 100
print(t)
for i in range(1, t + 1):
    nn = randint(70, primeListLength-1)
    zPrime = primeList[nn]
    pangram = pangramList[randint(0, pangramListLength-1)]
    f.write("Case #{}: {}\n".format(i, pangram))
    L = len(pangram) - 1
    alphaPrimeList = list(map(lambda x : primeList[x] ,sorted(sample(list(range(0,nn)), 26))))
    if len(alphaPrimeList) != 26:
        print("alphaPrimeList has {} primes".format(len(alphaPrimeList)))
    for jj in range(25):
        if alphaPrimeList[jj] >= alphaPrimeList[jj+1]:
            print("not ascending error!")
    primeOf = {}
    for j in range(0,26):
        primeOf[chr(ord('A') + j)] = alphaPrimeList[j]
    if len(primeOf) != 26:
        print("primeOf has {} keypairs".format(len(primeOf)))    
##    pangramPrime = list(map(lambda x : primeOf[x], list(pangram)))
    print("{} {}".format(zPrime + 1, L))
    for k in range(L):
##        cipher = pangramPrime[k] * pangramPrime[k+1]
        cipher = primeOf[pangram[k]] * primeOf[pangram[k+1]]
        if k == (L - 1):
            print(cipher)
        else:
            print(cipher, end=' ')    

f.close()



