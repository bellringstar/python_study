dV = 10

def decTobin(value):
    for j in range(3, -1, -1):
        r = value & (1<<j)
        if r:
            print(1,end='')
        else:
            print(0,end='')

decTobin(10)

def hexTodec(value):
    if value.isdigit():
        return int(s)
    else:
        return ord(value) - ord('A') + 10



