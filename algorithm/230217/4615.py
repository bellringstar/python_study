'''
오셀로게임
'''
# T = int(input())
# for tc in range(1, T+1):
#     N,M = map(int, input().split())
#     arr = [[0]*(N+2) for _ in rang(N+2)]
#     m = N//2
#     arr[m][m] = arr[m+1][m+1] = 2
#     arr[m+1][m] = arr[m][m+1] = 1
# 
#     for _ in range(M):
#         si, sj, d = map(int, input().split())
#         arr[si][sj] = d
#         for di, dj in ((-1,-1), (-1,0), (-1,1), (0,-1), (1,-1),(1,0),(1,1))
#             tlst = []
#             for mul in range(1, N):
#                 ni, nj = si+di*mul, sj+dj*mul
#                 if arr[ni][nj] == 0:
#                     break
#                 elif arr[ni][nj] != d:
#                     tlst.append((ni, nj))
#                 else:
#                     while tlst:
#                         ti, tj = tlst.pop()
#                         arr[ti][tj] = d
#                     break
#     bcnt = wcnt = 0
#     for lst in arr:
#         bcnt += lst.count(1)
#         wcnt += lst.count(2)
# 
#     print(f'#{tc} {bcnt} {wcnt}')

'''
i,j,검은
for 8방향:
    while 하얀색이 나올 때까지:
        ni, nj 를 찾는다.(ni,nj는 검은색)
    if 찾았다면:
        while ni, nj에서 i,j까지:
            검은색으로 변경
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2 - 1][N//2 - 1] = 2
    arr[N // 2 - 1][N // 2] = 1
    arr[N // 2][N // 2 - 1] = 1
    arr[N // 2][N // 2] = 2

    for _ in range(N):
        x, y, color = map(int, input().split())
        row,col = y-1, x-1
        #8방향에 놓은 돌과 다른 숫자가 있다면 숫자 변경


