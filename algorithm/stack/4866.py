def check(s_list):
    stack = []
    for s in s_list:
        stack.append(s)
        if len(stack) >= 2:
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop(); stack.pop()
            elif stack[-2] == '{' and stack[-1] == '}':
                stack.pop(); stack.pop()
    if stack:
        return 0
    else:
        return 1


T = int(input())

for test in range(T):
    check_list = ['(',')','{','}']
    lst_p = [s for s in input() if s in check_list]
    print(check(lst_p))








 