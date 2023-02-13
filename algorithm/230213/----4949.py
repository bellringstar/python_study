words = input()
check_list = ['(', ')', '[', ']']
def check(arr):
    stack = []
    for word in arr:
        if word == '(' or word == '[':
            stack.append(word)
        else:
            if stack:
                if word ==']' and stack[-1] == '[':
                    stack.pop()
                elif word == ')' and stack[-1] == '(':
                    stack.pop()
            else:
                return 'no'
    if stack:
        return 'no'
    else:
        return 'yes'

while words != '.':
    arr = [s for s in words.strip() if s in check_list]
    rst = check(arr)
    print(rst)
    print(arr)
    words = input()