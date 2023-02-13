'''
괄호검사
{,},(,)
{,(를 만나면 stack에 쌓는다
},)를 만나면 stack에서 pop 해서 짝이 맞는지 확인한다
1. 짝이 맞는다 계속 반복 진행
2. 짝이 틀리다. 종료

반복이 무사히 끝났는데 stack에 무언가 존재한다 = 실패
스택이 비었다 = 성공
'''
def check(lst):
    if not lst:
        return 0
    stack = []

    for s in lst:
        if s == '(' or s =='{':
            stack.append(s)
        else:
            if stack:
                if s == ')' and stack[-1] == '(' or s == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return 0
            else:
                return 0

    if stack:
        return 0
    else:
        return 1







T = int(input())
check_list = ['(', ')', '{', '}']
for tc in range(1, T+1):
    lst_p = [s for s in input() if s in check_list]
    rst = check(lst_p)
    print(f'#{tc} {rst}')
