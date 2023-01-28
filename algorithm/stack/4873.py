T = int(input())

for test in range(T):
    string = input()
    stack = [string[0]]
    for idx in range(1, len(string)):
        if stack and string[idx] == stack[-1]:
            stack.pop()
        else:
            stack.append(string[idx])
            
    print(len(stack))
        