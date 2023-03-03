def killer1(i, j):
    global N,M
    rst1 = 0
    rst1 += arr[i][j]
    for d in ((-1,0), (1,0), (0,-1), (0,1)):
        for k in range(1, M):
            new_i = i + k*d[0]
            new_j = j + k*d[1]
            if 0<=new_i<N and 0<=new_j<N:
                rst1 += arr[new_i][new_j]
    return rst1

def killer2(i,j):
    global N,M
    rst2 = 0
    rst2 += arr[i][j]
    for d in ((-1,-1),(-1,1),(1,-1),(1,1)):
        for k in range(1,M):
            new_i = i + k*d[0]
            new_j = j + k*d[1]
            if 0 <= new_i < N and 0 <= new_j < N:
                rst2 += arr[new_i][new_j]
    return rst2



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            rst1 = killer1(i,j)
            rst2 = killer2(i,j)
            ans = max(ans, rst1, rst2)
    print(f'#{tc} {ans}')