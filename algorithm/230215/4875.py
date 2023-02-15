'''
NxN크기, 출발지에서 목적지까지 가능? -> 1 불가능->0
2->3
'''

def possible(arr, s):
    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]
    rst = 0
    stack = []
    while True:
        for i in range(4):
            r = s[0] + dr[i]  # 행
            c = s[1] + dc[i]  # 열
            if r < N and r >= 0 and c < N and c >= 0:
                if arr[r][c] == 3:
                    return 1

                elif arr[r][c] == 0:
                    stack.append(s)
                    arr[r][c] = 1
                    s = (r, c)
                    for i in arr:
                        print(*i)
                    print()
                    break
        else:

            if stack:
                s = stack.pop()
            else:
                return 0

T = int(input())
for tc in range(1, T+1):
    s = 0
    N = int(input())
    arr = [list(map(int, input().rstrip())) for _ in range(N)]
    for row_idx, row in enumerate(arr):
        for col_idx, col in enumerate(arr[row_idx]):
            if col == 2:
                s = (row_idx, col_idx)


    if s:
        print(f'#{tc} {possible(arr, s)}')
    else:
        print(f'#{tc} 0')


def dfs(row, col):
    ST = []
    visited = [[False]*N for _ in range(N)]

    ST.append((row, col))
    visited[row][col] = True
    while ST:
        row, col = ST.pop()
        for dr, dc in [(-1, 0), (-1, 0), (0, 1), (0,-1)]:
            newR = row + dr
            newC = col + dc
            if 0<=newR<N and 0<=newC<N:
                if ARR[newR][newC] != 1 and not visited[newR][newC]:
                    if ARR[newR][newC] == 3:
                        return 1
                    ST.append((newR, newC))
                    visited[newR][newC] = True
    return 0


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int, input().rstrip())) for _ in range(N)]
    for i in range(N):
        if 2 in ARR[i]:
            row, col = i, ARR[i].index(2)


    print(f'#{tc} {dfs(row, col)}')