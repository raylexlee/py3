import numpy as np
import math
a = np.array([0.5,   0,   0])
b = np.array([  0, 0.5,   0])
c = np.array([  0,   0, 0.5])
y = np.array([0,1,0])
p = np.array([0.5,0.5,0.5])
v = np.cross(p, y)
u = v / np.linalg.norm(v)
d = math.sqrt(3)
p_o_y = math.acos(1 / d)
L = [np.array([x, y, z]) for x in [-0.5,0.5] for y in [-0.5,0.5] for z in [-0.5,0.5]]
def vectorRotatedBy(theta, x):
    u_x_x = np.cross(u, x)
    return u * np.dot(u, x) + np.cross(u_x_x, u) * math.cos(theta) + u_x_x * math.sin(theta)
T = int(input())
for i in range(1, T + 1):
    A = float(input())
    theta = p_o_y - math.acos(A / d)
    ans_a = vectorRotatedBy(theta, a)    
    ans_b = vectorRotatedBy(theta, b)
    ans_c = vectorRotatedBy(theta, c)
    print("Cast #{}:".format(i))
    print(*ans_a)
    print(*ans_b)
    print(*ans_c)
    if abs(np.linalg.norm(ans_a)-0.5) > 0.000001:
        print("Line 1 distance error")
    if abs(np.linalg.norm(ans_b)-0.5) > 0.000001:
        print("Line 2 distance error")
    if abs(np.linalg.norm(ans_c)-0.5) > 0.000001:
        print("Line 3 distance error")
    if np.dot(ans_a, ans_b) > 0.000001:
        print("Line 1 & 2 not perpenicular")    
    if np.dot(ans_c, ans_b) > 0.000001:
        print("Line 3 & 2 not perpenicular")    
    if np.dot(ans_a, ans_c) > 0.000001:
        print("Line 1 & 3 not perpenicular")    
    ans_L = [vectorRotatedBy(theta, P) for P in L]
    yOfL = [P[1] for P in ans_L]
    epsilon = abs(max(yOfL)-min(yOfL)-A)
    if epsilon > 0.000001:
        print("|{}-({})-{}| = {}".format(max(yOfL), min(yOfL), A, epsilon))
