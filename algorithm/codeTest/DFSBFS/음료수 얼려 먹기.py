import collections

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

# 0이면사 방문 안한 곳을 찾아서 BFS 반복 = BFS 실행 회수만큼 생성
visited = [[False]*M for _ in range(N)]
print(arr)

# def BFS(s):
#     global cnt
#     cnt += 1
#     q = collections.deque()
#     q.append(s)
#     visited[s[0]][s[1]] = True
#     while q:
#         now = q.popleft()
#         for d in ((-1,0), (1,0), (0,-1), (0,1)):
#             new_r = now[0] + d[0]
#             new_c = now[1] + d[1]
#             if 0<=new_r<N and 0<=new_c<M and arr[new_r][new_c] == '0' and not visited[new_r][new_c]:
#                 q.append((new_r, new_c))
#                 visited[new_r][new_c] = True
#
# cnt = 0
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == '0' and not visited[i][j]:
#             start = (i,j)
#             BFS(start)
#             continue
#
# print(cnt)

stack = []
def DFS(s):
    for row in arr:
        print(*row)
    print()
    stack.append(s)
    arr[s[0]][s[1]] = 1
    for d in ((-1,0),(1,0),(0,-1),(0,1)):
        new_r = s[0] + d[0]
        new_c = s[1] + d[1]
        if 0<=new_r<N and 0<=new_c<M and arr[new_r][new_c] == 0:
            DFS((new_r,new_c))

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            s = (i,j)
            DFS(s)
            cnt += 1

print(cnt)