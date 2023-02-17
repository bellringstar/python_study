for tc in range(1, 11):
    N, S = input().split()
    stack = []
    for c in S:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    rst = "".join(stack)
    print(f'#{tc} {rst}')