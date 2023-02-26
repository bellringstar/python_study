import collections,sys
input = sys.stdin.readline


def bfs(s, e):
    q = collections.deque()
    q.append((s, e))
    v[s][e] = arr[s][e]
    # v[e][s] = arr[e][s]
    visited[s] = 1
    visited[e] = 1
    print()
    while q:

        now = q.popleft() #현재 위치 s 다음위치 e3으로 이동
        for new_e in range(n+1):
            if not v[now[1]][new_e] and arr[now[1]][new_e] and not visited[new_e]:
                q.append((now[1],new_e))
                v[now[1]][new_e] = v[now[0]][now[1]] + arr[now[1]][new_e]
                visited[new_e] = 1
                # v[new_e][now[1]] = v[now[1]][now[0]] + arr[new_e][now[1]]




n = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]
v = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * 13

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    arr[a][b] = c
    arr[b][a] = c
ans = 0
bfs(1,1)
maxV = 0
for i in range(13):
    for j in range(13):
        if v[i][j] > maxV:
            maxV = v[i][j]
            max_i = i; max_j = j

v = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * 13
bfs(max_j,max_i)

for row in v:
    ans = max(ans,max(row))

v = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * 13
bfs(max_i,max_j)

for row in v:
    ans = max(ans,max(row))
print(ans)