'''
직선으로 연속으로 1이 나오는 갯수 최대
'''
def find_max(arr):
    global cnt_max
    for row in arr:
        cnt = 0
        for i in range(M):
            if row[i] == 1:
                cnt +=1
            else:
                if cnt > cnt_max:
                    cnt_max = cnt
                cnt = 0
        if cnt > cnt_max:
            cnt_max = cnt
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt_max = float('-inf')
    B = list(zip(*arr))  # 행렬변환
    find_max(arr)
    find_max(B)
    print(f'#{tc} {cnt_max}')



