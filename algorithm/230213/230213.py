'''
stack1
선형 자료 구조 / LIFO Last-in-First-Out 후입선출
대표 연산
1.삽입 = push
2.삭제 = pop
3.isEmpty
4.peek : top에 있는 원소(item) 반환
top = - 1로 설정 후 push => top += 1 /pop => top -= 1

def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

size = 10
stack = [0] * size
top -= 1

push(10, size)
top += 1
stack[top] = 20

def pop():
    global top
    if top == -1 :
        print('underflow')
        return 0
    else :
        top -= 1
        return stack[top+1]
print(pop())

if top > -1:
    top -= 1
    print(stack[top+1])



'''



