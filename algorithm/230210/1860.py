T = int(input())

for tc in range(1, 1+T):
    rst = 'Possible'
    N, M, K = map(int, input().split())
    sec = list(map(int, input().split()))
    arr = [0] * (max(sec) + 1)
    for i in range(M, len(arr), M):
        arr[i] += K
    sec.sort()
    for j in sec:
        arr[j] -= 1
        if sum(arr[:j+1]) < 0:
            rst = 'Impossible'


    print(f'#{tc} {rst}')


