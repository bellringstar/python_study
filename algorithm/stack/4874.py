# T = int(input())

# for test in range(T):

'''
1. 입려된 문자열 리스트로 받는다.
2. 숫자를 받으면 스택에 넣고 연산자를 만나면 스택에 있는 것을 pop 해서 계산하고 스택에 넣는다.
3. 스택에 넣는게 '.' 이면 스택에 있는 결과값을 출력한다.
'''
case = input().split()

stack = []
for num in case:
    if num.isdigit():
        stack.append(int(num))
    else:
        if len(stack) == 1 and num != '.':
            print('error')
            break
        if num == '.':
            rst = stack.pop()
            print(rst)
        else:
            a = stack.pop()
            b = stack.pop()
            if num == '+':
                stack.append(b+a)
            if num == '*':
                stack.append(b*a)
            if num == '/':
                stack.append(b//a)
            if num == '-':
                stack.append(b - a)

            
