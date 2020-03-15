pangramList = []
for i in range(0,337):
    pangramList.append(input())
for pangram in pangramList:
    if not pangram.isalpha():
        print("{} contains non-alpha".format(pangram)) 
    aList = sorted(dict.fromkeys(list(pangram)))
    if len(aList) != 26:
        print(pangram)
Min = min(map(lambda x : len(x), pangramList))
Max = max(map(lambda x : len(x), pangramList))
print("Minimum size = {}, Maxmimum size = {}".format(Min, Max))        
