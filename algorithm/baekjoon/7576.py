'''
익은 토마토 상하좌우도 하루 후 익는다. 혼자 저절로는 안익는다.
전부 다 익는데 며칠이 걸리는가.
#단계마다 +1, 끝난 후 0이 존재한다 = -1 0이 존재하지 않는다 = 최대값 - 1
'''
import sys, collections
input = sys.stdin.readline

def BFS():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    queue = collections.deque([])
    for s in start:
        queue.append(s)
    while queue:
        now = queue.popleft()
        for k in range(4):
            r = now[0] + dr[k]
            c = now[1] + dc[k]
            if 0<=r<N and 0<=c<M and arr[r][c] == 0:
                queue.append([r,c])
                arr[r][c] = arr[now[0]][now[1]] + 1
        for row in arr:
            print(*row)
        print()



M, N = map(int, input().split()) #M가로,N 세로
arr = [list(map(int, input().split())) for _ in range(N)]
start = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            start.append([i,j])

BFS()
ans = 0
for row in arr:
    for num in row:
        if num == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(row))
print(ans-1)

