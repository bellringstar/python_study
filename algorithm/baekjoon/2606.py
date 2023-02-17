# def dfs(v):
#     global cnt
#     stack = []
#     stack.append(v)
#     visited[v] = True
#     while stack:
#         # print(f'v: {v}')
#         # print(f'stack : {stack}')
#         # print(f'visited: {visited}')
#         for w in range(len(arr[v])):
#             if arr[v][w] == 1 and not visited[w]:
#                 visited[w] = True
#                 v = w
#                 stack.append(v)
#                 cnt += 1
#                 break
#         else:
#             v = stack.pop()


def dfs(v):
    global cnt
    visited[v] = 1
    print(f'visited = {visited}')
    for i in arr[v]:
        if not visited[i]:
            dfs(i)
            cnt += 1

N = int(input())
M = int(input())
# arr = [[0]*(N+1) for _ in range(N+1)]
arr = [[]*N for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0]*(N+1)
cnt = 0
# for _ in range(M):
#     n1, n2 = map(int, input().split())
#     arr[n1][n2] = 1
#     arr[n2][n1] = 1

dfs(1)
print(cnt)



