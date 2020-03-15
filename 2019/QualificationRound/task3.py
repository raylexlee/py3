# Title : Decipher crypto pangrams
# Date : 13 March 2020
# Author : Raylex Lee
#!/usr/bin/python3

import math

def Decipher(cipher_list):
    secretPrimes = []
    for i in range(1, len(cipher_list)):
        secretPrimes.append(math.gcd(cipher_list[i-1], cipher_list[i]))
    secretPrimes.insert(0, cipher_list[0] // secretPrimes[0] )
    secretPrimes.append(cipher_list[-1] // secretPrimes[-1])
    primesList = sorted(list(dict.fromkeys(secretPrimes)))
    acutalLetter = {}
    for i in range(len(primesList)):
        acutalLetter[primesList[i]] = chr(ord('A') + i)
    return ''.join(map(lambda x : acutalLetter[x], secretPrimes))    

def ReadDataOutputAnswer():
    t = int(input())
    for i in range(1, t+1):
        n, l = [int(s) for s in input().split(" ")]
        cipher = [int(s) for s in input().split(" ")]
        print("Case #{}: {}".format(i, Decipher(cipher)))

if __name__ == '__main__':
    ReadDataOutputAnswer()