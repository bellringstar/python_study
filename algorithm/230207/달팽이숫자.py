T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    row = 0
    col = 0
    dx= [1,0,-1,0]
    dy= [0,-1,0,1]
    d = [1,1,-1,-1]
    cnt = 0
    for i in range(1, N*N+1):
        arr[row][col] = i
        tmp_row = row
        tmp_col = col
        if cnt % 2 :
            row += d[cnt%4]
        else:
            col += d[cnt%4]

        if row < 0 or row > N-1 or col <0 or col > N -1 or arr[row][col] != 0 :
            row = tmp_row + dx[cnt%4]
            col = tmp_col + dy[cnt%4]
            cnt += 1

    print(f'#{tc}')
    for i in arr:
        for j in i:
            print(j,end=' ')
        print()