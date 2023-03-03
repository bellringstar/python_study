T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    ans = sum(arr[N//2])
    k = 1
    while k <= N//2:
        for i in range(N//2-1, -1, -1):
            ans += sum(arr[i][k:N-k])
            ans += sum(arr[N-i-1][k:N-k])
            k += 1

    print(f'#{tc} {ans}')