import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

# print(arr)

def dfs(v):
    stack.append(v)
    visited[v] = True
    if len(stack) == 5:
        return True
    # print(stack)
    while stack:
        for w in arr[v]:
            if not visited[w]:
                return dfs(w)

        else:
            stack.pop()




for i in range(N):
    stack = []
    visited = [False] * N
    if dfs(i):
        print(1)
        break
else:
    print(0)