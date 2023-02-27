import sys,collections
input = sys.stdin.readline
def BFS(s):
    q = collections.deque()
    q.append((s,0))
    visited[s] = 1
    while q:
        now = q.popleft()
        for new in arr[now[0]]:
            if not visited[new[0]]:
                visited[new[0]] = visited[now[0]] + new[1]
                q.append(new)
            else:
                if visited[new[0]] > visited[now[0]] + new[1]:
                    visited[new[0]] = visited[now[0]] + new[1]

V, E = map(int, input().split())

arr = [[] for _ in range(V+1)]
start = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))
visited = [0] * (V+1)
BFS(start)
for i in range(1, V+1):
    if visited[i]:
        print(visited[i] - 1)
    else:
        print('INF')

