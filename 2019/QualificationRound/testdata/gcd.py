def gcd(a, b):
    while b:
        a, b = b, divmod(a, b)[1]
    return a

for a in range(100, 120):
    for b in (80, 90):
        print("gcd({}, {}) = {}".format(a, b, gcd(a,b)))        
