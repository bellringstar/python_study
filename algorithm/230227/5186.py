T = int(input())
for tc in range(1, T+1):
    N = float(input())
    cnt = 0
    rst = ''
    while True:
        N = N * 2
        cnt += 1
        if cnt == 13:
            rst = 'overflow'
            break
        if N%1 == 0:
            rst += '1'
            break
        elif N > 1:
            N -= 1
            rst += '1'
        else:
            rst += '0'
    print(f'#{tc} {rst}')
