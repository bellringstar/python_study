# def stack(arr, *t):
#     if t[0] == 'push':
#         arr.append(int(t[1]))
#     elif t[0] == 'top':
#         if len(arr) == 0:
#             print(-1)
#         else:
#             print(arr[-1])
#     elif t[0] == 'size':
#         print(len(arr))
#     elif t[0] == 'empty':
#         if len(arr) != 0:
#             print(0)
#         else:
#             print(1)
#     elif t[0] == 'pop':
#         if len(arr) == 0:
#             print(-1)
#         else:
#             print(arr.pop())
#
#


#-------------------시간초과----------------------------
import sys
input = sys.stdin.readline

def stack(arr, *t):
    global top
    if t[0] == 'push':
        top += 1
        arr[top] = t[1]
    elif t[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(arr[top])
    elif t[0] == 'size':
        print(top+1)
    elif t[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif t[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(arr[top])
            top -= 1

N = int(input())
arr = [0] * N
top = -1
for i in range(N):
    stack(arr, *input().split())
