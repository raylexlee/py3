# Title : Decipher crypto pangrams
# Version 2 : modified from task3.py
# Filename : task3_v2.py
# Date : 15 March 2020
# Author : Raylex Lee
#!/usr/bin/python3

import math

def Decipher(cipher_list):
    secretPrimes = []
    for i in range(1, len(cipher_list)):
        secretPrimes.append(math.gcd(cipher_list[i-1], cipher_list[i]))
#    secretPrimes.insert(0, cipher_list[0] // secretPrimes[0] )
#    secretPrimes.append(cipher_list[-1] // secretPrimes[-1])
    secretPrimes.insert(0, divmod(cipher_list[0] ,secretPrimes[0])[0] )
    secretPrimes.append(divmod(cipher_list[-1] , secretPrimes[-1])[0])
    check_list = []
    for i in range(len(secretPrimes)-1):
        check_list.append(secretPrimes[i] * secretPrimes[i+1])
    for y in range(len(cipher_list)):
        if cipher_list[y] != check_list[y]:
            print(y, end=' ')
    primesList = sorted(list(dict.fromkeys(secretPrimes)))
    primesListLength = len(primesList)
    if primesListLength != 26:
        print("{} primes are recorded.".format(primesListLength))
    acutalLetter = {}
    for i in range(len(primesList)):
        acutalLetter[primesList[i]] = chr(ord('A') + i)
    return ''.join(map(lambda x : acutalLetter[x], secretPrimes))    

def ReadDataOutputAnswer():
    t = int(input())
    for i in range(1, t+1):
        n, l = [int(s) for s in input().split(" ")]
        cipher = [int(s) for s in input().split(" ")]
        cl = len(cipher)
        if cl != l :
            print("L = {}, but we have read {} numbers!".format(l, cl))
        print("Case #{}: {}".format(i, Decipher(cipher)))

if __name__ == '__main__':
    ReadDataOutputAnswer()