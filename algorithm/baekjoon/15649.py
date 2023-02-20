# import itertools
# N, M = map(int, input().split()) #1~N까지 중복없이 M개 순열
#
# A = list(range(1, N+1))
#
# rst = list(itertools.combinations(A, M))
#
# for i in rst:
#     print(*i)


N, M = map(int, input().split()) #1~N까지 중복없이 M개 순열

def dfs(v,d=1):
    global M
    visited[v] = True
    stack.append(v)
    if d == M:
        print(*stack)
        return
    for i in range(v, N+1):
        if not visited[i]:
            dfs(i, d+1)
            stack.pop()
            visited[i] = False


for i in range(1, N+1):
    visited = [False] * (N + 1)
    stack = []
    dfs(i)
