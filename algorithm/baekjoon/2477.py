'''
참외밭 넓이 구하기
'''

import sys
input = sys.stdin.readline
K = int(input()) #단위 참외수
#1:서쪽 2:동쪽 / 3:남쪽 4:북쪽
arr = []
for _ in range(6):
    arr.append(tuple(map(int, input().split())))
arr = arr*2
for idx in range(6):
    if arr[idx][0] == arr[idx+2][0] and arr[idx+1][0] == arr[idx+3][0]:
        minus = arr[idx + 1][1] * arr[idx + 2][1]
        break


x = 0
y = 0
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        x = max(x, arr[i][1])

    if arr[i][0] == 3 or arr[i][0] == 4:
        y = max(y, arr[i][1])

ans = (x * y - minus) * K

print(ans)