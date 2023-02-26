import sys
input = sys.stdin.readline

ex = input().rstrip()

op = ('+', '-')

stack = []
number = ''
for num in ex:
    if num in op:
        stack.append(int(number))
        number = ''
        stack.append(num)
    else:
        number += num
stack.append(int(number))

plus_stack = []
minus_stack = []
lst = plus_stack
for num in stack:
    if num == '-':
        lst = minus_stack
    elif num != '+':
        lst.append(num)

rst = sum(plus_stack) - sum(minus_stack)

print(rst)


