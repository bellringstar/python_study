import sys,collections
input = sys.stdin.readline


def BFS(i, j):
    global cnt
    cnt += 1
    q = collections.deque()
    q.append((i, j))
    while q:
        now = q.popleft()
        arr[now[0]][now[1]] = 0
        for dr, dc in ((1, 0), (-1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)):
            new_r = now[0] + dr
            new_c = now[1] + dc
            if 0 <= new_r < h and 0 <= new_c < w and arr[new_r][new_c] == 1:
                arr[new_r][new_c] = 0
                q.append((new_r, new_c))


while True:
    w, h = map(int, input().split())
    if w ==0 and h ==0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)] #1이땅
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                BFS(i,j)
    print(cnt)

