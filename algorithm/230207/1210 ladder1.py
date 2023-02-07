import sys
sys.stdin = open('inputladder1.txt', 'r')

for _ in range(10):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    dx = [1, 0, 0] #하,좌,우
    dy = [0, -1, 1]
    start_pos = []
    for i in range(len(arr[0])):
        if arr[0][i] == 1:
            start_pos.append(i)
    for start in start_pos:
        cnt = [[False] * 100 for _ in range(100)]
        # print(start)
        x = 0
        y = start
        cnt[x][y] = True
        while x<99:
            for d in range(2,-1,-1): #우,좌,하 판단
                new_x = x + dx[d]
                new_y = y + dy[d]
                if new_x<100 and new_x>=0 and new_y<100 and new_y>=0:
                    if arr[new_x][new_y] >= 1 and cnt[new_x][new_y] == False:
                        tmp = d
                        x = new_x
                        y = new_y
                        cnt[x][y] = True
                        break
        if arr[x][y] == 2:
            print(f'#{T} {start}')
            break


