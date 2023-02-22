

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# T = int(input())
#
# def BFS(i,j):
#     lst = []
#     lst.append(arr[i][j])
#     queue = collections.deque()
#     queue.append([i,j])
#     visit[i][j] = 1
#     while queue:
#         now = queue.popleft()
#         for k in range(4):
#             new_i = now[0] + dr[k]
#             new_j = now[1] + dc[k]
#             if 0<=new_i<N and 0<=new_j<N and arr[new_i][new_j] == arr[now[0]][now[1]] + 1 and not visit[new_i][new_j]:
#                 new = (new_i, new_j)
#                 queue.append(new)
#                 lst.append(arr[new_i][new_j])
#                 visit[new[0]][new[1]] = 1
#
#     return min(lst), len(lst)
import collections,sys
# sys.stdin = open('1861input.txt','r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
def BFS(i,j):
    queue = collections.deque()
    queue.append((i,j))
    visit[i][j] = 1
    lst = []
    lst.append(arr[i][j])
    while queue:
        now = queue.popleft()
        for k in range(4):
            new_r = now[0] + dr[k]
            new_c = now[1] + dc[k]
            if 0<=new_r<N and 0<=new_c<N:
                if arr[new_r][new_c] == arr[now[0]][now[1]] + 1 and visit[new_r][new_c] == 0:
                    lst.append(arr[new_r][new_c])
                    visit[new_r][new_c] = 1
                    queue.append((new_r,new_c))
    return min(lst), len(lst)


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    maxL = 0
    s = []
    for i in range(N):
        for j in range(N):
            start, max_len = BFS(i,j)
            if max_len >= maxL:
                maxL = max_len
                s.append((maxL, start))
    s.sort(key=lambda x: (x[0], -x[1]))

    print(s)



