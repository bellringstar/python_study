import sys, collections
input = sys.stdin.readline
queue = collections.deque()

N, M = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(i,j):
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            new_i = i + dr[k]
            new_j = j + dc[k]
            if 0<=new_i<N and 0<=new_j<M:
                if arr[new_i][new_j] != 0 and not visited[new_i][new_j]:
                    visited[new_i][new_j] = True
                    arr[new_i][new_j] = arr[i][j] + 1
                    queue.append((new_i, new_j))


BFS(0,0)
print(arr[N-1][M-1])
