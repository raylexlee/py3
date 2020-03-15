import math
x = []
for i in range(4):
  x.append(int(input()))
a = x[0] * x[1]
b = x[1] * x[2]
c = math.gcd(a, b)
print("{}".format(c))
