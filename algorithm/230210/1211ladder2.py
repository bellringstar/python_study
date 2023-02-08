import sys
sys.stdin = open('1211input.txt', 'r')

dx = [1, 0, 0]
dy = [0, -1, 1]
for _ in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    start_pos = []
    for i in range(len(arr[0])):
        if arr[0][i] == 1:
            start_pos.append(i)
    cnt_arr = []
    for start in start_pos:
        cnts = [[False] * 100 for _ in range(100)]
        cnt = 0
        x = 0
        y = start
        while x < 100:
            cnts[x][y] = True
            cnt += 1
            if x == 99:
                break
            for i in range(2,-1,-1): #우,좌,하 우선순위 판단
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x < 100 and new_x>=0 and new_y < 100 and new_y>=0:
                    if arr[new_x][new_y] == 1 and cnts[new_x][new_y] == False:
                        x = new_x
                        y = new_y
                        break
        cnt_arr.append([start, cnt])
        cnt_arr.sort(key=lambda x:x[1])
    print(f'#{T} {cnt_arr[0][0]}')



