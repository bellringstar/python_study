'''
1 = 갈수있다 0 = 갈수없다 시작 (1,1) 목적지 (N,M)
최소 칸
'''

from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]


def BFS(s):
    global N,M
    cnt = 0
    q = deque()
    q.append(s)
    while q:
        now = q.popleft()
        r = now[0]
        c = now[1]
        arr[r][c] = 0
        for d in ((-1,0),(1,0),(0,-1),(0,1)):
            new_r = r + d[0]
            new_c = c + d[1]
            if (new_r, new_c) == (N-1,M-1):
                return cnt
            if 0<=new_r<N and 0<=new_c<M and arr[new_r][new_c] :
                q.append((new_r,new_c))
                arr[new_r][new_c] = 0
                for row in arr:
                    print(*row)
                print()
                cnt += 1

rst = BFS((0,0))

print(rst)