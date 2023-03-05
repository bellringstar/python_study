# T = int(input())
# for tc in range(1, T+1):
#     arr = [input() for _ in range(5)]
#     max_length = 0
#     for row in arr:
#         if max_length < len(row):
#             max_length = len(row)
#
#     for idx in range(5):
#         arr[idx] += '*' * (max_length - len(arr[idx]))
#
#     new_arr = list(zip(*arr))
#     rst = ''
#     for row in new_arr:
#         for s in row:
#             if s != '*':
#                 rst += s
#     print(f'#{tc} {rst}')
#
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = [input() for _ in range(5)]
#     max_length = 0
#     for row in arr:
#         max_length = max(max_length, len(row))
#
#     rst = ''
#     for i in range(max_length): #열
#         for j in range(5):
#             if i < len(arr[j]):
#                 rst += arr[j][i]
#     print(f'#{tc} {rst}')

# T = int(input())
# for tc in range(1,T+1):
#     lst = [list(input()) for _ in range(5)]
#
#     ans = ''
#     max_L = 0
#     for row in lst:
#         max_L = max(max_L, len(row))
#     for i in range(max_L):
#         for j in range(5):
#             # if 0 <= j < len(lst[i]):
#             try:
#                 ans += lst[j][i]
#             except:
#                 continue
#
#     print(ans)