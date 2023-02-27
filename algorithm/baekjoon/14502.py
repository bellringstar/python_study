import sys, collections, copy
input = sys.stdin.readline
q = collections.deque()

N, M = map(int, input().split()) #N = 세로 = 행, M = 가로 = 열
arr = [list(map(int, input().split())) for _ in range(N)]

'''
0인 곳 3곳을 1로 변경
DFS -> 0의 개수를 센다
'''
def bfs():
    for idx in two_idx:
        q.append(idx)
    while q:
        now = q.popleft()
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            new = (now[0] + dr, now[1] + dc)
            if 0<=new[0]<N and 0<=new[1]<M:
                if lab[new[0]][new[1]] == 0:
                    lab[new[0]][new[1]] = 2
                    q.append(new)


zero_idx = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero_idx.append((i,j))
two_idx = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            two_idx.append((i,j))

zero_L = len(zero_idx)
rst = 0
for i in range(zero_L):
    for j in range(i+1,zero_L):
        for k in range(j+1,zero_L):
            lab = copy.deepcopy(arr)
            zero1 = zero_idx[i]
            zero2 = zero_idx[j]
            zero3 = zero_idx[k]
            # print(f'zero1:{zero1}, zero2:{zero2}, zero3:{zero3}')
            lab[zero1[0]][zero1[1]] = 1
            lab[zero2[0]][zero2[1]] = 1
            lab[zero3[0]][zero3[1]] = 1
            bfs()
            cnt = 0
            for row in lab:
                cnt += row.count(0)
            rst = max(rst,cnt)
print(rst)