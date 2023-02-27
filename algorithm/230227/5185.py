T = int(input())
for tc in range(1, T+1):
    N, X = input().split()
    ans = ''
    for num in X:
        if num.isdigit():
            b = int(num)
        else:
            b = ord(num) - ord('A') + 10

        for j in range(3,-1,-1):
            r = b & 1<<j
            if r:
                ans += '1'
            else:
                ans += '0'
    print(f'#{tc} {ans}')





