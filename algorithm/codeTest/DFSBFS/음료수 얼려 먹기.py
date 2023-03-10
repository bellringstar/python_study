import collections

N, M = map(int, input().split())

arr = [input() for _ in range(N)]

# 0이면사 방문 안한 곳을 찾아서 BFS 반복 = BFS 실행 회수만큼 생성
visited = [[False]*M for _ in range(N)]


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

def DFS(s)

