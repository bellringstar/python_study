'''
N번 W x H 배열 ( H행, W열)
0 빈공간
구슬 스타트 = [0][j] j 0-> W
구슬이 벽돌의 좌표에 간다 = 상하좌우 벽돌 수 -1 만큼 제거
ex)1 = 자기만 제거 3 = 상하좌우 2개 추가 제거
제거 후 빈공간 -> 벽돌의 행 증가
남은 벽돌의 최소 개수
타겟 = [x][y] -> [x-1][y] = 0 이면서, 연쇄작용이 가장 큰 줄
'''
def renew(arr, H, W):
    '''
    2. [0,1,1,0,0,3,4,5,0,1] -> 뒤부터 순환 0을 만나면 0 이전에 0이 아닌것과
    '''
    for col in range(W):
        for row in range(H):
            if arr[row][col] == 0:
                for k in range(row,0,-1):
                    arr[k][col], arr[k-1][col] = arr[k-1][col], arr[k][col]

def attack(arr, target, target_x, target_y):
    dx = [1, 0, 0] #하 좌 우
    dy = [0, -1, 1]
    '''
    delta 갱신: delta 만큼 cnt번 이동하다 1보다 큰 수를 만나면 cnt 갱신
    '''
    while cnt > 0:
        for i in range(3):
            cnt = target
            for j in range(cnt):
                new_x = target_x + j * dx[i]
                new_y = target_y + j * dy[i]
                if new_x < H and new_x > 0 and new_y < W and new_y > 0:
                    cnt -= 1
                    if arr[new_x][new_y] > 1:
                        cnt = arr[new_x][new_y]
                        target_x = new_x
                        target_y = new_y
                    arr[new_x][new_y] = 0
    for row in arr:
        print(*row)

def find_target(arr):
    pass


# import sys
# sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [[0]*W for _ in range(H)]
    for i in range(H):
        arr[i] = list(map(int,input().split()))

    for case in range(N):
        # target = find_target(arr) # 타겟을 찾는다
        target, target_x, target_y = map(int, input().split())
        attack(arr,target,target_x,target_y) #타겟을 공격해 별돌 삭제
        renew(arr, H, W) #벽돌이 삭제 된 후 arr를 재정렬








