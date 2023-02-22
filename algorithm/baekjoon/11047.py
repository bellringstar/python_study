import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [0] * N
for i in range(N):
    lst[N-i-1] = int(input())

cnt = 0
for num in lst:
    while K >= num:
        cnt += K // num
        K = K % num


print(cnt)
