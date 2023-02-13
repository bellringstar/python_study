
def push(item, size:int):
    global  top
    if top == size-1:
        print('full')
    else:
        top += 1
        stack[top] = item

def pop():
    global top
    if top == -1:
        print('is empty')
        return -1
    else:
        tmp = stack[top]
        stack[top] = 0
        top -= 1
        return tmp


T = int(input())
for tc in range(1, T+1):

    word = input()
    size = len(word)
    stack = [0] * size
    top = -1

    for s in word:
        if s == stack[top]:
            pop()
        else:
            push(s, size)
    rst = len(stack) - stack.count(0)
    print(f'#{tc} {rst}')