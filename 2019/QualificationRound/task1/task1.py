def Split(digit):
    if digit == '4': return '1', '3'
    return digit, '0'
def ReadDataAndAnswerQuestion():
    t = int(input())
    for i in range(1, t+1):
        n = input()
        part = list(n)
        a = int(''.join(map(lambda x : Split(x)[0], part)))  
        b = int(''.join(map(lambda x : Split(x)[1], part)))
        print("Case #{}: {} {}".format(i, a, b))

if __name__ == '__main__':
    ReadDataAndAnswerQuestion()