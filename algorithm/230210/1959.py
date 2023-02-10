import sys
sys.stdin = open('1959input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N >= M:
        sum_arr =[]
        for i in range(N-M+1):
            sum_p = 0
            for j in range(M):
                sum_p += A[i+j] * B[j]
            sum_arr.append(sum_p)

    else:
        sum_arr = []
        for i in range(M-N+1):
            sum_p = 0
            for j in range(N):
                sum_p += A[j] * B[i+j]
            sum_arr.append(sum_p)

    max_v = sum_arr[0]
    for num in sum_arr:
        if num > max_v:
            max_v = num

    print(f'#{tc} {max_v}')