import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10000)

dr = [-1,0,1,0]
dc = [0,1,0,-1]

# def dfs(row, col):
#     global cnt
#     cnt += 1
#     stack.pop()
#     arr[row][col] = 0
#     for i in range(4):
#         new_row = row + dr[i]
#         new_col = col + dc[i]
#         if 0<=new_row<N and 0<=new_col<M and arr[new_row][new_col] == 1:
#             stack.append([new_row,new_col])
#             arr[new_row][new_col] = 0
#             dfs(new_row, new_col)

def dfs(row, col):
    global cnt
    cnt += 1
    stack.append([row, col])
    arr[row][col] = 0
    while stack:
        row,col = stack.pop()
        for i in range(4):
            new_row = row + dr[i]
            new_col = col + dc[i]
            if 0<=new_row<N and 0<=new_col<M and arr[new_row][new_col] == 1:
                stack.append([new_row,new_col])
                arr[new_row][new_col] = 0


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        col, row = map(int, input().split())
        arr[row][col] = 1
    rst = []
    for i in range(N):
        for j in range(M):
            stack = []
            cnt = 0
            if arr[i][j] == 1:
                # stack.append([i,j])
                dfs(i,j)
                rst.append(cnt)
    print(len(rst))

