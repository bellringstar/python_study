#
#
# def row_check(arr):
#     for i in range(N):
#         cnt_row = [0] * 9
#         for j in range(N):
#             if cnt_row[arr[i][j] - 1] == 1:
#                return False
#             cnt_row[arr[i][j] - 1] = 1
#         else:
#             continue
#     return True
#
# def col_check(arr):
#     for i in range(N):
#         cnt_col = [0] * 9
#         for j in range(N):
#             if cnt_col[arr[j][i] - 1] == 1:
#                 return False
#             cnt_col[arr[j][i] - 1] = 1
#         else:
#             continue
#     return  True
#
# def cross_check(arr,k=0):
#     k = 0
#     while k < 9:
#         for start in range(0,9,3):
#             cnt_cross = [0] * 9
#             for i in range(start, start+3):
#                 for j in range(k, k+3):
#                     if cnt_cross[arr[i][j] - 1] == 1:
#                         return False
#                     cnt_cross[arr[i][j] - 1] = 1
#         k += 3
#     return True
#
#
# import sys
# sys.stdin = open('1974input.txt', 'r')
#
# T = int(input())
# N = 9
# for tc in range(1, T+1):
#     arr = [0] * N
#     for i in range(N):
#         arr[i] = list(map(int, input().split()))
#     rst = 0
#     if row_check(arr) and col_check(arr) and cross_check(arr):
#         rst = 1
#     print(f'#{tc} {rst}')


'''
한줄의 모든 숫자가 1번만 -> 중복의 문제
set을 사용해 중복판정
'''
