import sys
sys.stdin = open('input1풍선.txt', 'r')

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_lst = [list(map(int, input().split())) for _ in range(N)]
    sum_max = []
    for i in range(N):
        for j in range(M):
            sumV = N_lst[i][j]
            for k in range(4):
                new_i = i + dx[k]
                new_j = j + dy[k]
                if new_i >=0 and new_i < N and new_j >=0 and new_j < M:
                    sumV += N_lst[new_i][new_j]
            sum_max.append(sumV)
    maxV = sum_max[0]
    for value in sum_max:
        if value > maxV:
            maxV = value
    print(f'#{tc} {maxV}')
