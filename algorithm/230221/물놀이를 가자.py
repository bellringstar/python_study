import collections

def BFS():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while queue:
        for row in arr:
            print(*row)
        print()
        now = queue.popleft()
        for k in range(4):
            r = now[0] + dr[k]
            c = now[1] + dc[k]
            if 0<=r<N and 0<=c<M and arr[r][c] == 0:
                queue.append([r,c])
                arr[r][c] = arr[now[0]][now[1]] + 1


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                arr[i][j] = 0

    queue = collections.deque([])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                arr[i][j] = 1
                queue.append([i,j])

    BFS()
    ans = 0
    for row in arr:
        ans += sum(row)
    ans -= N*M
    print(ans)




