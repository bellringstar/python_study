import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
cnt = 1
rst = [0] * (N+1)
for _ in range(N):
    a,b,c,r = map(int, input().split())
    a = 1000 - a
    for i in range(a,a-c,-1):
        for j in range(b,b+r):
            arr[i][j] = cnt
    cnt += 1


for idx in range(1,N+1):
    ans = 0
    for row in arr:
        ans += row.count(idx)
    print(ans)

