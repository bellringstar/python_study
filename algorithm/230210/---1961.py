'''
목적기 기준으로 원본이 어떻게 변하는가
좌표를 사용 할 것이므로 좌표 기준 확인
arr2[i][j] = arr1[N-j-1][i]
'''

import sys
sys.stdin = open('1961input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    a1 = [[0] * N for _ in range(N)]
    a2 = [[0] * N for _ in range(N)]
    a3 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]
            a2[i][j] = arr[N-1-i][N-1-j]
            a3[i][j] = arr[j][N-1-i]

    for a,b,c in zip(a1, a2, a3):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')

