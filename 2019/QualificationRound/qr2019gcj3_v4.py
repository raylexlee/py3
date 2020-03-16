# Task : Qualifiction Round 2019 Google Code Jam 3rd problem
# Title : Decipher crypto pangrams
# Date : 17 March 2020
# Bug fix of qr2019gcj3.py dated 16 March 2020
# Abandon FillupEmptySecretePrime Recursion because of stack overflow
# Author : Raylex Lee
#!/usr/bin/python3

# import math
def gcd(a, b):
    while b:
        a, b = b, divmod(a, b)[1]
    return a

def Decipher(cipher_list):
    L = len(cipher_list)
    # Initialize secretPrime[x] = None for all x = 0 .. L
    secretPrime = dict.fromkeys(range(L + 1))
    missingPrimeIndexSet = {0, L}
    for i in range(1, L):
        if cipher_list[i-1] != cipher_list[i]:
            secretPrime[i] = gcd(cipher_list[i-1], cipher_list[i])
        else:
            missingPrimeIndexSet.add(i)    
    def AttemptFillUpMissingPrime(pos):
        if (pos - 1) >= 0:
            if secretPrime[pos-1] != None:
                secretPrime[pos] = divmod(cipher_list[pos-1], secretPrime[pos-1])[0]
                return True
        if (pos + 1) <= L:
            if secretPrime[pos+1] != None:
                secretPrime[pos] = divmod(cipher_list[pos], secretPrime[pos+1])[0]
                return True
        return False        
    # Fill up those missing secretPrime[x] == None ** in action now
    while missingPrimeIndexSet:
        for e in missingPrimeIndexSet:
            if AttemptFillUpMissingPrime(e):
                break
        missingPrimeIndexSet.remove(e)       
    secretPrimeList = list(map(lambda x : secretPrime[x], range(0, L+1)))
    primesList = sorted(list(dict.fromkeys(secretPrimeList))) 
    acutalLetter = {}
    for i in range(len(primesList)):
        acutalLetter[primesList[i]] = chr(ord('A') + i)
    return ''.join(map(lambda x : acutalLetter[secretPrime[x]], range(0, L+1)))    

def ReadDataOutputAnswer():
    t = int(input())
    for i in range(1, t+1):
        n, l = [int(s) for s in input().split(" ")]
        cipher = [int(s) for s in input().split(" ")]
        print("Case #{}: {}".format(i, Decipher(cipher)))

if __name__ == '__main__':
    ReadDataOutputAnswer()