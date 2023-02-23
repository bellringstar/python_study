import sys
sys.stdin = open('input사칙.txt','r')




def postorder(root):
    if root:
        postorder(left_c[root])
        postorder(right_c[root])
        ex.append(tree[root])

def calulator(arr):
    stack = []
    for num in arr:
        if num.isdigit():
            stack.append(int(num))
        else:
            if num == '+':
                v1 = stack.pop()
                v2 = stack.pop()
                v = v2 + v1
                stack.append(v)
            elif num == '-':
                v1 = stack.pop()
                v2 = stack.pop()
                v = v2 - v1
                stack.append(v)
            elif num == '*':
                v1 = stack.pop()
                v2 = stack.pop()
                v = v2 * v1
                stack.append(v)
            elif num == '/':
                v1 = stack.pop()
                v2 = stack.pop()
                v = v2 / v1
                stack.append(v)
    return int(stack.pop())

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    left_c = [0] * (N + 1)
    right_c = [0] * (N + 1)
    for _ in range(N):
        arr = list(input().split())
        if len(arr) > 2:
            tree[int(arr[0])] = arr[1]
            left_c[int(arr[0])] = int(arr[2])
            right_c[int(arr[0])] = int(arr[3])
        else:
            tree[int(arr[0])] = arr[1]
    ex = []
    postorder(1)
    rst = calulator(ex)
    print(f'#{tc} {rst}')
    '''
    print(tree)
    print(left_c)
    print(right_c)
    [0, '-', '-', 10, 88, 65]
    [0, 2, 4, 0, 0, 0]
    [0, 3, 5, 0, 0, 0]
    '''

