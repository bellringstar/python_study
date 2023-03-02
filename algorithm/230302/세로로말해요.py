T = int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    max_L = 0
    rst = ''
    i = 0
    for row in arr:
        max_L = max(max_L, len(arr))

    while i <= max_L:
        for row in arr:
            if i < len(row):
                rst += row[i]
        i += 1

    print(f'#{tc} {rst}')