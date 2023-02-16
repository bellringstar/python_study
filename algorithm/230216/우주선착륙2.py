import sys
sys.stdin = open('2input.txt', 'r')


def check(x,y):
    center_x = x
    center_y = y
    max_cnt = 0
    min_cnt = 0

    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    for d in range(8):
        i = x + di[d]
        j = y + dj[d]
        if 0<=i<N and 0<=j<M:
            if arr[center_x][center_y] < arr[i][j]:
                max_cnt += 1
            elif arr[center_x][center_y] > arr[i][j]:
                min_cnt += 1

            if max_cnt > 4:
                return 0
            if min_cnt == 4:
                return 1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start = []
    for i in range(N):
        for j in range(M):
            start.append([i,j])

    rst = 0
    for x,y in start:
        if check(x,y):
            rst += 1

    print(f'#{tc} {rst}')