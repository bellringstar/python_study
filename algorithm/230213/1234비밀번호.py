import sys
sys.stdin = open('1234input.txt', 'r')


for tc in range(1, 11):
    N, M = input().split()
    stack = []
    for num in M:
        if stack:
            if num == stack[-1]:
                stack.pop()
            else:
                stack.append(num)
        else:
            stack.append(num)
    rst = ''.join(stack)
    print(f'#{tc} {rst}')
