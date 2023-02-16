def postfix(string):
    icp = {'+':1 ,'*':2}
    stack = []
    exp = ''
    for s in string:
        if s.isdigit():
            exp += s
        else:
            if not stack:
                stack.append(s)
            else:
                while stack and icp[stack[-1]] >= icp[s]:
                    exp += stack.pop()
                stack.append(s)

    while stack:
        exp += stack.pop()
    return exp

def cal(string):
    stack = []
    for s in string:
        if s.isdigit():
            stack.append(int(s))
        else:
            if s == '+':
                a1 = stack.pop()
                a2 = stack.pop()
                a = a2 + a1
                stack.append(a)

            else:
                a1 = stack.pop()
                a2 = stack.pop()
                a = a2 * a1
                stack.append(a)

    return stack[-1]




for tc in range(1, 11):
    N = int(input())
    string = input()
    rst = cal(postfix(string))
    print(f'#{tc} {rst}')