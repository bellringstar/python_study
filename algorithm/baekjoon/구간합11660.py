N, M = map(int, input().split())

arr = [[0] * N for _ in range(N)]
S = [[0] * N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

tmp = 0
for row in range(N):
    S[row][0] = arr[row][0] + tmp
    for i in range(1, N):
        S[row][i] = S[row][i-1] + arr[row][i]
    tmp = S[row][-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1; y1 -=1; x2 -= 1; y2 -=1
    if (x1, y1) == (x2, y2):
        rst = arr[x1][y1]
    elif (x1,y1) == (0,0):
        rst = S[x2][y2]
    else:
        a = S[x2][y2]
        b = S[x2][y1-1]
        c = S[x1][y2]
        d = S[x1][y1-1]
        rst = a - b + c - d
    print(rst)
