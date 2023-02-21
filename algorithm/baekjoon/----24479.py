import sys
input = sys.stdin.readline


N, M, R = map(int, input().split())
visited = [False] * (N + 1)
arr= [[] for _ in range(N+1)]
lst = [0] * (N + 1)
cnt = 1
stack = []
# def dfs(v):
#     global cnt
#     lst[v] = cnt
#     visited[v] = True
#     for w in arr[v]:
#         if not visited[w]:
#             cnt += 1
#             dfs(w)

stack = []
def dfs(v):
    global cnt
    stack.append(v)
    lst[v] = cnt
    visited[v] = True
    while stack:
        v = stack.pop()
        for w in arr[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True
                cnt += 1
                lst[w] = cnt
                break

for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

for row in arr:
    row.sort()

dfs(R)
for i in range(1, N+1):
    print(lst[i])

