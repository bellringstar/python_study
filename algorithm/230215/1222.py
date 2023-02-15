def cal(string):
    stack = []
    ex = ''
    for num in string:
        if num.isdigit():
            ex += num
        else:
            if stack:
                ex += stack.pop()
                stack.append(num)
            else:
                stack.append(num)
    ex += stack.pop()
    rst = 0
    for s in ex:
        if s.isdigit():
            stack.append(int(s))
        else:
            a = stack.pop() + stack.pop()
            stack.append(a)

    return stack[-1]




for tc in range(1, 11):
    L = int(input())
    string = input()
    rst = cal(string)
    print(f'#{tc} {rst}')
