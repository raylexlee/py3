def switch(w):
    if w == 'E': return 'S'
    return 'E'

t = int(input())
for i in range(1, t+1):
    n = int(input())
    p = input()
    a = ''.join(map(lambda x : switch(x), list(p)))
    print("Case #{}: {}".format(i, a))