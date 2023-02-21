import sys
sys.stdin = open('input.txt', 'r')
#16x16 x방향 : c 증가 y방향: r증가 = x,y = r,c
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
queue = []
def bfs(i,j):
    queue.append([i,j])
    arr[i][j] = -1
    while queue:
        now = queue.pop()
        for k in range(4):
            r = now[0] + dr[k]
            c = now[1] + dc[k]
            if arr[r][c] == 0 or arr[r][c] == 3:
                queue.append([r,c])
                arr[r][c] = arr[now[0]][now[1]] - 1


for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                s = [i, j]
            elif arr[i][j] == 3:
                e = [i, j]

    bfs(s[0], s[1])

    ans = 1
    if arr[e[0]][e[1]] == 3:
        ans = 0

    print(f'#{T} {ans}')