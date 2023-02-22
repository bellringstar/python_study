import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
s = e = 0
for num in lst:
    if s < num:
        s = num
    e += num


while s<=e:
    cnt = 0
    sum = 0
    mid = (s+e)//2
    for i in range(N):
        if sum + lst[i] > mid:
            cnt += 1
            sum = 0
        sum += lst[i]
    if sum != 0:
        cnt += 1

    if cnt > M :
        s = mid + 1
    else:
        e = mid - 1

print(s)


