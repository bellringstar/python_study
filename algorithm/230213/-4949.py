while True:
    text = input()
    stack = []
    if text == '.':
        break

    for s in text:
        if s =='(' or s == '[' :
            stack.append(s)
        elif s == ']' :
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif s == ')' :
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if stack:
        print('no')
    else:
        print('yes')