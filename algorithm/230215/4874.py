T = int(input())

def cal(arr):
    stack = []
    op =['+','-','*','/']
    for num in arr[:-1]:
        if num.isdigit():
            stack.append(int(num))
        elif num in op:
            if len(stack) >=2:
                a1 = stack.pop()
                a2 = stack.pop()
                if num == '+':
                    stack.append(a2+a1)
                elif num == '-':
                    stack.append(a2-a1)
                elif num == '*':
                    stack.append(a2*a1)
                elif num == '/':
                    stack.append(a2//a1)
            else:
                return 'error'
    if len(stack) > 1:
        return 'error'

    return stack[-1]



for tc in range(1, T+1):
    arr = input().split()
    print(f'#{tc} {cal(arr)}')
