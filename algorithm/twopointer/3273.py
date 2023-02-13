# n = int(input())
# arr = list(map(int, input().split()))
# target = int(input())
#
# left, right = 0, n - 1
# cnt = 0
# arr.sort()
# #1 2 3 5 7 10 11 12
# while left < right:
#     if arr[left] + arr[right] > target:
#         right -= 1
#     elif arr[left] + arr[right] < target:
#         left += 1
#     else:
#         cnt += 1
#         left += 1
#         right = n - 1
#
# print(cnt)

#------------시간초과--------