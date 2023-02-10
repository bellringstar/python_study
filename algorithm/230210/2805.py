import sys
sys.stdin = open('2805input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    mid = N // 2
    sum_v = 0
    for i in range(mid, -1, -1):
        for j in range(mid - i, N - mid + i):
            if i == mid:
                sum_v += int(arr[i][j])
            else:
                sum_v += int(arr[i][j]) + int(arr[N-i-1][j])
    print(f'#{tc} {sum_v}')