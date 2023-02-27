'''
최대한 적은 종류 비행기로 모든 국가 여행
'''
def DFS(v):
    global cnt
    stack = []
    visited = [False] * (N + 1)
    stack.append(v)
    visited[v] = True
    while stack:
        v = stack[-1]
        for w in arr[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True
                cnt += 1
                break
        else:
            stack.pop()

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    cnt = 0
    DFS(1)

    print(cnt)