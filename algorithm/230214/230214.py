class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.check = 0

    def push(self, item):
        self.top = Node(item, self.top)
        self.check += 1
        print(f'{item} 삽입 top:{self.check}')

    def pop(self):
        if self.isempty():
            return -1
        item = self.top.item
        self.top = self.top.next
        self.check -= 1
        print(f'{item} pop, top:{self.check}')
        return item


    def isempty(self):
        return self.top == None

    def peak(self):
        if self.isempty():
            return -1
        print(f'{self.top.item} top:{self.check}')
        return self.top.item


'''
DP 동적 계획법 -> 최적화 문제
작은 부분 문제들로 나눠 모두 해결한 후에 그 해들을 이용하여 보다 큰 문제를 해결 -> 반복해 최종 해를 구한다

'''
def f(i, k): #재귀의 기본 틀: 현재치, 목표치
    if i == k: #목표에 도달하면
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, k)

A = [10, 20, 30]
B = [0] * 3

f(0, 3)

'''
DFSBFS(깊이우선탐색)
갈림길의 위치를 기록해놔야한다.
1. 시작정점 v를 결정하여 방문
2. 정점v에 인접한 정점 중에서
2-1. 방문하지 않은 정점 w가 있으면 정점 v를 스택에 push하고 정점 w를 반문한다.
그리고 w를 v로 하여 다시 2를 반복
2-2. 방문하지 않은 정점이 없으면 탐색방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로하여 다시 2 반복
3. 스택이 공백이 될 때까지 2를 반복

visites[], stack[] 초기화
DFSBFS(v):
    시작점, v 방문
    visited[v] <- True
    while {
        if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            push(v);
            v <- w;
            visites[w] <- True
        else
            if (스택이 비어 있지 않으면)
                v <- pop(stack)
            else
                break
    }
end DFSBFS()
'''

def dfs(v):
    stack = []
    visited = [False] * ValueError

    stack.append(v)
    while stack:
        v = stack.pop()
        for w in G[v]:
            if not visited[w]:
                stack.append(w)

