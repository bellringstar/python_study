'''
2Darray
2차원 array는 곱셈연산으로 만들면 안된다
[[0]*3]*3 (x) [[0]*3 for i in range(3)] (o)

배열의 순회
행 우선 순회
for i in range(n):
    for j in range(m):
        arr[i][j]

열 우선 순회
for i in range(m):
    for j in range(n):
        arr[j][i]

지그재그 순회
for i in range(n):
    for j in range(m):
        arr[i][j + (m-1-2*j)*(i%2)]


2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법 (델타 이용)
arr[0...N-1][0...N-1] NxN 배열
di[] <- [0, 0, -1, 1] 좌우상하
dj[] <- [-1,-1, 0, 0]
for i : 0 -> N-1:
    for j : 0-> N-1:
        for k in range(4):
            ni <- i +di[k]
            nj <- j +dj[k]
            if 0 <= ni <N and 0<=nj<N:# 유효한 인덱스
                test(arr[ni][nj])

'''

