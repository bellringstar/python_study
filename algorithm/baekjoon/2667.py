N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
rst = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(row,col):
    global cnt
    cnt += 1
    arr[row][col] = 0
    stack.pop()
    for i in range(4):
        new_r = row + dr[i]
        new_c = col + dc[i]
        if 0<=new_r<N and 0<=new_c<N and arr[new_r][new_c] == 1:
            # print(new_r,new_c)
            stack.append((new_r,new_c))
            dfs(stack[-1][0], stack[-1][1])

for row in range(N):
    for col in range(N):
        if arr[row][col] == 1:
            stack = []
            cnt = 0
            stack.append((row,col))
            # print(row,col)
            dfs(row,col)
            rst.append(cnt)

print(len(rst))
rst.sort()
for num in rst:
    print(num)