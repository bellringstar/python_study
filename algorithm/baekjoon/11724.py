# N, M = map(int, input().split())
# arr = [[0]*(N+1) for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     arr[a][b] = 1
#     arr[b][a] = 1
# visited = [False] * (N + 1)
#
# def dfs(v):
#     stack = []
#     stack.append(v)
#     visited[v] = True
#     while stack:
#         v = stack.pop()
#         for idx, w in enumerate(arr[v]):
#             if w == 1 and not visited[idx]:
#                 visited[idx] = True
#                 stack.append(idx)

#


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# def DFS(v):
#     visited[v] = True
#     for w in A[v]:
#         if not visited[w]:
#             DFS(w)

def DFS(v):
    stack = []
    stack.append(v)
    visited[v] = True
    while stack:
        v = stack.pop()
        for w in A[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True




for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)


cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        DFS(i)

print(cnt)
