'''
계산기1
문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산
1. 중위표기법의 수식을 후위표기법으로 변경(스택이용)
2. 후위표기법의 수식을 스택을 이용하여 계산

중위표기법을 후위표기법으로 변환하는 방법
우선순위에 따라 괄호를 친 다음 연산자를 괄호 밖으로 뺸다.
1. 토큰 하나 가져오기
2. 스택연산 push()
토큰이 연산자면 스택 top과 비교해 우선순위가 높으면 push / 피연산자면 스택 패스
스택 내 더 높거나 같은 우선순위가 있다면 자신보다 낮은애 까지 pop 후 push
우선순위: '(' 밖에서는 우선순위가 가장 높지만 스택 내에서는 가장 낮다.
3. top을 변경
4. 닫는괄호를 만난다 -> 여는 괄호를 만날때까지 pop 그 후 여는 괄호는 버린다.

후위표기법을 계산하는 법
숫자는 스택에 push 연산자를 만나면 스택에서 (pop2 연산 pop1) 뒤 처리 후(순서 주의) 스택에 push
토큰에 수식이 없으면 stack의 값 pop
'''
'''
백트래킹
해를 찾는 도중에 막히면 되돌아가서 다시 해를 찾아 가는 기법 -> 최적화, 결정 문제
결정문제: 문제의 조건을 만족하는 해가 존재하는지 여부를 yes 또는 no
ex)미로, n-Queen, Map coloring, Subset Sum ....

현재 위치 stack에 저장((1,0) 오른쪽) -> 이동
이 과정 반복 후 더 이상 징행이 불가능하면 갈림길까지 pop

백트래킹 vs DFS
백트래킹은 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않는다 = 가지치기(Prunning)
불필요한 경로를 조기에 차단
promising 유망한가? 유망하지 않으면 노드의 부모로 되돌아간다.

1. 상태공간 트리의 깊이 우선 탐색을 실기
2. 각 노드가 유망한지를 점검한다.
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.
def checknode(v):
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for u in each child of v:
                checknode(u)
                
                
부분집합 구하기
powerset 2^n개
원하는 부분집합을 찾을때 유망하지 않은 것을 만나면 그 루트는 생략  
'''


# NUMS = [1, 2, 3]
# N = 3
# a = [-1] * N
# #[0,0,0] ... [1,2,3]
# def construct_candidates(c):
#     c[0] = 0
#     c[1] = 1
#     return 2
#
#
# def backtrack(a, k):
#     c = [-1] * 2
#     if k == N:
#         sum_a = 0
#         for i,val in enumerate(a,1):
#             if val == 1:
#                 sum_a += i
#         print(a, sum_a)
#         return
#     nc = construct_candidates(c)
#     for i in range(nc):
#         a[k] = c[i]
#         backtrack(a, k+1)
#
#
# backtrack(a, 0)


c = [0, 1]
def partial(k, curS):

    if k == N:
        print(a)
        return

    a[k] = 0
    partial(k+1, curS)
    a[k] = 1
    partial(k+1, curS+nums[k])
