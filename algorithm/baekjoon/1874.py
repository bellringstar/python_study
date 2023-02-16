n = int(input())
stack = []
num = 1
rst = []

for i in range(n):
    val = int(input())
    if val >= num:
        while num <= val:
            stack.append(num)
            rst.append('+')
            num += 1
        stack.pop()
        rst.append('-')
    else:
        v = stack.pop()
        if v == val:
            rst.append('-')
        else:
            rst = ['NO']
            break

for i in rst:
    print(i)