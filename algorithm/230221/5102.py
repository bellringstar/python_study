import sys
sys.stdin = open('sample_input5102.txt','r')

queue = []
def bfs(v):
    queue.append(v)
    visited[v] = 0
    while queue:
        v = queue.pop(0)
        for w in arr[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    S, G = map(int, input().split())
    bfs(S)
    print(f'#{tc} {visited[G]}')