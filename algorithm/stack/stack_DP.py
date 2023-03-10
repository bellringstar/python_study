'''
stack : 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
스택에 저장된 자료는 선형구조를 가짐
선형구조 : 자료 간의 관계가 1대1의 관계
비선형구조 : 자료 간의 관계가 1대 N의 관계를 가짐 ex)트리
스택에서는 마지막에 삽입한 자료를 가장 먼저 꺼냄 LIFO 후입선출

필요조건
1. 자료를 선형으로 저장할 저장장소 ex)배열, 리스트
마지막에 삽입된 원소의 위치 = top
연산
1.삽입 : push
2.삭제 : pop
3.isEmpty: 공백?
4.peek: top에 있는 item 반환

스택 구현 고려사항
1. 리스트를 사용하여 스택을 구현하는 경우
장점: 구현이 용이하다
단점: 리스트의 크기를 변경하는 작업은 내부적으로 큰 overhead 발생 작업으로 많은 시간이 소요
-> 해결법 
1.리스트의 크기가 변동되지 않도록 배열처럼 크기를 미리 정해놓고 사용하는 방법
2.동적 연결리스트를 이용하여 저장소를 동적으로 할당하여 스택을 구현하는 방법
장점: 구현이 용이하다
단점: 리스트로 구현하는 것보다 구현이 복잡하다

응용1. 괄호검사
1. 왼쪽 괄호의 개수가 오른쪽 괄호의 개수가 같아야 함
2. 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 함
3. 괄호 사이에는 포함 관계만 존재함
스택을 이용해 '('는 push ')'를 만나면 pop 하면 마지막에 빈 스택이라면 옳바른 상황

응용2. 함수 호출 관리
프로그램에서의 함수 호풀과 복귀에 따른 수행 순서를 관리
가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조. = 스택과 유사
1. 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임에 저장해
시스템 스택에 삽입
2. 함수의 실행이 끝나면 시스템 스택의 top 원소를 삭제 하면서 프레임에 저장되어있던 복귀주소를 확인하고 복귀
3. 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 됨

재귀호출
1. 자기 자신을 호출하여 순환 수행
2. 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀 호출 방식을 사용하여 함수를 만들면
프로그램의 크기를 줄이고 간단하게 작성할 수 있음
3. 하지만 디버깅이 어렵고 잘못 작성시 수행시간이 오래걸리게 됨

Memoization
컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장하여 매번 다시 계산하지 않도록 하여 전체적인 실행속도 상승
DP(동적계획법)의 핵심
ex)피보나치수열
#memo를 위한 리스트 생성
#memo[0]을 0으로 memo[1]을 1로 초기화

def fibo1(n):
    global memo
    if n>=2 and len(memo)<=n :
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]
memo = [0, 1]

DP(동적계획법) Dynamic Programming
그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘
1. 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결
2. 최종적으로 원래 주어진 입력읨 문제를 해결

def fibo2(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

DP 구형 방식
1. recursive 방식 (fibo1())
재귀적 구조는 내부에 시스템 호출 스택을 사용하는 overhead가 발생할 수 있음
2. iterative 방식 (fibo2())
Memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적

DFSBFS(깊이 우선 탐색)
비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요
1. 깊이 우선 탐색 DFSBFS(Depth First Search)
2. 너비 우선 탐색 BFS(Breadth First Search)

DFS방법
1. 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색
2. 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아옴
3. 다른 방향의 정점으로 탐색을 계속 반복하여 결구 모든 정점을 방문하여 순회
->가장 마지막에 만났던 갈림길의 정점으로 되돌아 가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택을 사용

1. 시작정점 v를 결정하여 방문
정점 v에 인접한 정점 중에서
1-1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문
-> w를 v로 하여 다시 반복
1-2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 반복

visited[], stack[] 초기화
DFSBFS(v)
    v 방문;
    visited[v] <-true;
    do {
        if (v의 인접 정점 중 방문 안 한 w 찾기)
            push(v)
        while(w){
            w 방문;
            visited[w]<-true;
            push(w)
            v<-w;
            v의 인접 정점 중 방문 안 한 w 찾기
        }
        v<-pop(stack);
    }while(v)
end DFSBFS()
다시 돌아오기 위해 사용한 자료구조 = 스택



계산기
문자열 수식 계산의 일반적 방법
1. 중위표기법의 수식을 후위표기법으로 변경
스택 이용
중위표기법 : 연산자를 피연산자의 가운데 표연하는 방법 ex)A+B
2. 후위표기법의 수식을 스택을 이용하여 계산
후위표기법 : 연산자를 피연산자 뒤에 표기하는 방법 ex)AB+

ex)A*B-C/D ->((A*B)-(C/D)) 괄호 -> ((AB)*(CD)/)- 괄호 내부의 연산자들을 괄호 밖으로 뺀다 -> AB*CD/-
사람이 하기는 쉽지만 프로그래밍으로 처리하기는 어려움 ->변환 알고리즘 개발

변환 알고리즘1 스택사용
1. 입력받은 중위표기식에서 토큰을 읽음
2. 토큰이 피연산자이면 토큰을 출력
3. 토큰이 연산자(괄호포함)일 경우
 우선순위가 높으면 ->스택에 push
우선순위가 안 높으면 -> 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰 연산자를 push
만약 top에 연산자가 없으면 push
4. 토큰이 ')' 일 경우 -> 스택 top에 '('가 올 때까지 스택에 pop 연산을 수행 -> pop한 연산자를 출력 but '('를 만나면 pop만 하고 출력은 안함
5. 중위표기식에 더 읽을것이 없다면 중지, 있다면 처음부터 반복
6. 스택에 남아 있는 연산자를 모두 pop하여 출력
스택 밖의 '('는 우선 순위가 가장 높으며 스택 안의 '('는 우선 순위가 가장 낮음
토큰: 수식에서 의미 있는 최소의 단위
피연산자는 후위표기법 수식에 출력됨/ 연산자는 스택을 거쳐감/ 연산자를 stack에 쌓기 위해서는 스택 안에 낮은 우선순위 연산자가 있어야함

후위표기법의 수식을 스택을 이용하여 계산
1. '피연산자'를 만나면 스택에 push함
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push함
3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력

문자열로 된 수식 계산 = eval() 하지만 사용하지 않는 것이 좋음

백트래킹
해를 찾는 도중에 '막히면', 즉 해가 아니면 되돌아가서 다시 해를 찾는 기법
-> 최적화 문제와 결정 문제(yes/no 답하는 문제) 해결가능

ex)미로찾기
1. 입구와 출구가 주어진 미로에서 입구부터 출구까지의 경로를 찾는 문제
2. 이동할 수 있는 방향은 4방향으로 제한
2차 리스트로 미로 상태 표현 -> 현 위치, 이동방향(시계방향 우선) stack에 push ->이동이 불가능해 진다면 stack pop하며 뒤로 돌아간다.

백트래킹 vs 깊이 우선 탐색
백트래킹: 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더이상 그 경로를 따라가지 않음 -> 시도 회수 줄인다. = 가지치기(Prunning)
불필요한 경로 조기 차단
N!가지의 경우의 수를 가진 문제에 대해 백트레킹에 가하면 일반적으로 경우의 수가 줄어들이만 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하므로 처리 불가능
모든 후보를 검사하지 않는다.
어떤 노드의 유망성을 점검한 후에 유망(Promising)하지 않다고 결정되면 그 노드의 부모로 돌아가 다음 자식 노드로 감
어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 함
해담의 가능성이 있다 = 유망하다

깊이 우선 탐색: 모든 경로를 추적. N!가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐생을 가하면 처리 불가능
모든 후보를 검사

백트래킹 알고리즘 절차
1. 상태 공간 Tree의 깊이 우선 검색을 실시
2. 각 노드가 유망한지를 점검
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가 검색을 계속

ex) n queen 문제
n*n의 정사각형 안에 n개의 queen을 배치하는 문제
모든 queen은 자신의 일직선상 및 대각선상에 아무 것도 놓이지 않아야 함
def checknode(v): #node
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for u in each child of v:
                checknode(u)

이 문제에서 순수한 깊이 우선 탐색 = 155노드/백트래킹 = 27노드

ex) Power Set
어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합
구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합 개수는 2^n이 나옴
n개의 원소가 들어있는 집합의 2^n개의 부분집합을 만들 때, True또는 Fasle 값을 가지는 항목들로 구성된 n개의 리스트를 만드는 방법사용
리스트의 i번째 항목은 i번째 원소가 부분집합의 값인지 아닌지를 나타내는 값
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a,k) #답이면 원하는 작업을 한다
    else:
        k+=1
        ncadidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    print(',end='')
    for i in range(k+1):
        if a[i]:
            print(i, end=' ')
    print(')')

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 3) #3개의 원소

ex)백트래킹 순열
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        for i in range(1, k+1):
            print(a[i], end=' ')
        print()
    else:
        k+=1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncnadidates


분할 정복 알고리즘
Divide: 해결할 문제를 여러 개의 작은 부분으로 나눔
Conquer: 나눈 작은 문제를 각가 해결
Combine: 필요하다면 해결된 해답을 모음

거듭제곱 알고리즘: O(n)
def Power(Base, Exponent):
    if Base == 0 : return 1
    result = 1 # Base^0은 1
    for i in range(Exponent):
        result *= Base
    return result

-> 분할정복기반 거듭제곱 알고리즘 : O(log2n)
def Power(Base, Exponet):
    if Exponent == 0 or Base == 0:
        return 1
    if Exponent % 2 == 0:
        NewBase = Power(Base, Exponent/2)
        return NewBase * NewBase
    else:
        NewBase = Power(Base,(Exponent-1)/2)
        return (NewBase*NewBase)*Base

합병 정렬 vs 퀵 정렬
주어진 리스트를 두 개로 분할하고 각각을 정렬
차이점
합병 정렬 : 분할할 때 단순하게 두 부분으로 나눔. 각 부분 정렬이 끝난 후,합병이란 후처리 작업 필요
퀵 정렬: 분할할 때 기준 아이템(Pivot)을 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킴. 각 부분 정렬이 끝난 후, 후처리가 필요 없음

def quickSort(a, begin, end):
    if begin < end:
        p = pratition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
def partition(a, begin, end): #피봇 구하기
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L<R:
        while(a[L]<a[pivot] and L < R): L +=1 #L은 왼쪽부터 증가해가며 큰 값을 찾는다
        while(a[R]>=a[pivot] and L < R): R -=1 #R은 오른쪽부터 감소해가며 작은 값을 찾는다
        if L<R:
            if L==pivot: pivot = R
            a[L],a[R] = a[R],a[L]
    a[pivot],a[R] = a[R],a[pivot] #피봇보다 작은 값은 피봇 왼쪽, 큰 값은 오른쪽에 가도록 함
    return R
        
퀵정렬은 최악의 경우 O(n^2) = 합병정렬보다 안좋음
하지만 평균적으로 O(nlogn)이기 때문에 quick 정렬이라 부름


'''
