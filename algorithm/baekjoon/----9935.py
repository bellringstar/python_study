# import sys
# input = sys.stdin.readline
#
# string = input().rstrip()
# ex = input().rstrip()
# N = len(ex)
#
# while ex in string:
#     string = string.replace(ex,'')
#
# if string:
#     print(string)
# else:
#     print('FRULA')
#=------시간초과

import sys
input = sys.stdin.readline

stack = []
string = input().rstrip()
ex = input().rstrip()
N = len(ex)
j = 0
for i in range(len(string)):
    stack.append(string[i])
    if stack[-1] == ex[-1] and len(stack) >= N:
        if "".join(stack[len(stack)-N:]) == ex:
            for _ in range(N):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")



