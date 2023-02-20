import sys, collections
input = sys.stdin.readline



stack = []
queue = collections.deque()
N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)
for row in arr:
    row.sort()

def dfs(v):
    stack.append(v)
    visited[v] = True
    while stack:
        v = stack.pop()
        print(v, end=' ')
        for w in arr[v]:
            if not visited[w]:
                # stack.append(w)
                # visited[w] = True
                # break
                dfs(w)
def bfs(v):
    queue.append(v)
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for w in arr[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)


visited = [False] * (N+1)
dfs(V)
print()

visited = [False] * (N+1)
bfs(V)