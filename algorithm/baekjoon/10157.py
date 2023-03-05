'''
가로 C, 세로 R
좌표 표기 주의
(1,1) 부터 시작해 시계방향 증가
K번쨰의 좌표는?
'''


import sys
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

arr = [[0] * C for _ in range(R)]
n = 0
d = [(-1,0), (0,1), (1,0), (0,-1)]
value = 1
x = 0
y = R - 1
rst = 0
while arr[y][x] == 0:
    arr[y][x] = value
    if arr[y][x] == K:
        rst = (x+1,R-y)
        break
    x = x + d[n][1]
    y = y + d[n][0]
    if 0<=x<C and 0<=y<R and arr[y][x] == 0:
        value += 1
    else:
        x = x - d[n][1]
        y = y - d[n][0]
        n = (n+1)%4
        x = x + d[n][1]
        y = y + d[n][0]
        value += 1
if rst == 0:
    print(rst)
else:
    print(*rst)

