def post(string):
    isp = {'(': 3, '+': 1, '*': 2}
    icp = {'(': 0, '+': 1, '*': 2}
    stack = []
    ex = ''
    for c in string:
        if c.isdigit():
            ex += c
        else:
            if not stack or c == '(':
                stack.append(c)
            elif c == ')':
                while stack[-1] != '(':
                    ex += stack.pop()
                stack.pop()
            elif icp[stack[-1]] < icp[c]:
                stack.append(c)
            elif icp[stack[-1]] >= icp[c]:
                while stack and icp[stack[-1]] >= icp[c]:
                    ex += stack.pop()
                stack.append(c)
    while stack:
        ex += stack.pop()
    return ex


def cal(string):
    stack = []
    for c in string:
        if c.isdigit():
            stack.append(int(c))
        else:
            if c == '+':
                a = stack.pop()
                b = stack.pop()
                val = b + a
                stack.append(val)
            elif c == '*':
                a = stack.pop()
                b = stack.pop()
                val = b * a
                stack.append(val)
    return stack[-1]



for tc in range(1,11):
    N = int(input())
    case = input()
    rst = cal(post(case))
    print(f'#{tc} {rst}')