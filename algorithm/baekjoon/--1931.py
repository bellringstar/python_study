import sys
input = sys.stdin.readline

N = int(input())
arr = [[0,0] for _ in range(N)]

for i in range(N):
    s,e = map(int, input().split())
    arr[i][0] = e
    arr[i][1] = s

arr.sort()
#[[4, 1], [5, 3], [6, 0], [7, 5], [8, 3], [9, 5], [10, 6], [11, 8], [12, 8], [13, 2], [14, 12]]

cnt = 0
e = -1


for i in range(N):
    if arr[i][1] >= e:
        e = arr[i][0]
        cnt += 1

print(cnt)