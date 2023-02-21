import sys
sys.stdin = open('sample_input5105.txt','r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = []
def bfs(i,j):
    queue.append([i,j])
    while queue:
        now = queue.pop(0)
        for k in range(4):
            r = now[0] + dr[k]
            c = now[1] + dc[k]
            if 0<=r<N and 0<=c<N and (arr[r][c] == 0 or arr[r][c] == 3):
                queue.append([r,c])
                arr[r][c] = arr[now[0]][now[1]] + 1
        # for row in arr:
        #     print(*row)
        # print()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                e = [i,j]
            elif arr[i][j] == 2:
                s = [i,j]

    bfs(s[0], s[1])
    ans = arr[e[0]][e[1]] - 3
    print(f'#{tc} {ans}')



