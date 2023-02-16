def group(start, end):
    if start == end:
        return start

    a = group(start, (start + end) // 2)
    b = group((start + end) // 2 + 1, end)
    return win(a, b)  # 가위바위보 실시


def win(x, y):
    if arr[x] == arr[y]:  # 비긴 경우
        return x
    elif arr[x] - arr[y] == 1 or arr[x] - arr[y] == -2:  # x가 이긴 경우
        return x
    return y




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    rst = group(0,N-1) + 1
    print(f'#{tc} {rst}')


