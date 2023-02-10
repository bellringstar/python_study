# import sys
# sys.stdin = open('1979input.txt', 'r')
# 
# T = int(input())
# dx = [0, 1] #우,하
# dy = [1, 0]
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [0] * N
#     for i in range(N):
#         arr[i] = (list(map(int, input().split())))
#     rst = 0
# 
#     for i in range(N):
#         cnt_row = 0
#         x = i
#         y = 0
#         while True: #행 우선 판단
#             if arr[x][y] == 1: #1일때
#                 cnt_row += 1
#             else:
#                 if cnt_row == K:
#                     rst +=1
#                 cnt_row = 0
#             if y+1 >= N:
#                 if cnt_row == K:
#                     rst +=1
#                 cnt_row = 0
#                 break
#             new_x = x + dx[0]
#             new_y = y + dy[0]
#             if new_x < N and new_y < N:
#                 x = new_x
#                 y = new_y
#     for j in range(N):
#         x = 0
#         y = j
#         cnt_col = 0
#         while True:
#             if arr[x][y] == 1:
#                 cnt_col += 1
#             else:
#                 if cnt_col == K:
#                     rst += 1
#                 cnt_col = 0
#             if x+1 >= N:
#                 if cnt_col == K:
#                     rst +=1
#                 cnt_col = 0
#                 break
#             new_x = x + dx[1]
#             new_y = y + dy[1]
#             if new_x < N and new_y < N:
#                 x = new_x
#                 y = new_y
# 
#     print(f'#{tc} {rst}')


'''
1을 만나면 cnt 증가 cnt가 끝나면 길이 비교 -> cnt가 끝나는 경우 = 0을 만난다 혹은 경계를 만난다.
0을 만나거나 경계를 만난다 -> 두 경우를 따저야함 -> 차라리 경계에 0을 채워 넣어서 하나로 압축
가로확인 후 세로 확인을 해야한다 1. 열 우선 탐색 2. 전치행렬 i>j -> arr[i]<->arr[j] 3. zip으로 가로세로 변환
rst = 0
for row in arr:
    cnt = 0
    if n in row:
        if n == 1:
            cnt += 1
        else:
            if cnt == k:
                rst += 1
                cnt = 0
'''