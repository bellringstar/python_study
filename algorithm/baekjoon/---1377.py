# import sys
# input = sys.stdin.readline
#
# N = int(input())
# A = []
# for i in range(N):
#     A.append(int(input()))
#
#
#
# cnt = 0
# for i in range(N,-1,-1):
#     changed = False
#     cnt += 1
#     for j in range(i-1):
#         if A[j] > A[j+1]:
#             A[j], A[j+1] = A[j+1], A[j]
#             changed = True
#     if changed == False:
#         print(cnt)
#         break
#시간초과


