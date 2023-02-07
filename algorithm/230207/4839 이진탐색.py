def binaryS(target, end):
    cnt = 0
    start = 1
    if end < target:
        return 1000
    while start<=end:
        mid = (start + end)//2
        if mid == target:
            return cnt
        elif mid > target:
            cnt += 1
            end = mid
        else:
            cnt += 1
            start = mid

    return 1000

T = int(input())
for tc in range(1, T+1):
    winner = ''
    P,A,B = map(int, input().split())
    count_A = binaryS(A,P); count_B = binaryS(B,P)
    if count_A < count_B:
        winner = 'A'
    elif count_A == count_B:
        winner = 0
    else:
        winner = 'B'

    print(f'#{tc} {winner}')