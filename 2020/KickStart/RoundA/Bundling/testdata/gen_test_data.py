import random
random.seed(19111010)
T = random.randint(85,100)
M = 5
print(T)
for i in range(1,T):
    rTwo = random.randint(0,5)
    rFive = random.randint(0,5)
    if rTwo == 0 and rFive == 0:
        rTwo = 1
    N = (2 ** rTwo) * (5 ** rFive)
    K = (2 ** random.randint(0,rTwo))*(5 ** random.randint(0,rFive))
    print(N, K)
    for j in range(N):
        s = ''.join([chr(ord('A')+random.randint(0, 25)) for k in range(random.randint(1,M))])
        print(s)