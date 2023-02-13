import sys
input = sys.stdin.readline

T = int(input())
def VPS(arr):
    stack = []
    for s in arr:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                return 'NO'
    if stack:
        return 'NO'
    else:
        return 'YES'


for tc in range(1, T+1):
    arr = list(input().rstrip())
    rst = VPS(arr)
    print(rst)