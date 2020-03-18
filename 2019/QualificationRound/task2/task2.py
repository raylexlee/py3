t = int(input())
for i in range(1, t+1):
    n = int(input())
    p = input()
    a = ''.join(map(lambda x : 'E' if x == 'S' else 'S', list(p)))
    print("Case #{}: {}".format(i, a))