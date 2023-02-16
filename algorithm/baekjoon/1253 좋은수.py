# import sys
# input = sys.stdin.readline
#
# N = int(input())
# A = list(map(int, input().split()))
# A.sort()
# cnt = 0
# if N<=2:
#     cnt = 0
# else:
#     for i in range(2, N):
#         s = 0
#         e = i-1
#         while s<e:
#             if A[s] + A[e] < A[i]:
#                 s += 1
#             elif A[s] + A[e] > A[i]:
#                 s -= 1
#             else:
#                 cnt += 1
#                 break
#
#
# print(cnt)
#---------------시간초과
import sys
input = sys.stdin.readline

N = int(input())
rst = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N):
    target = A[k]
    s = 0
    e = N-1
    while s<e:
        if A[s] + A[e] == target:
            if s != k and e !=k:
                rst += 1
                break
            elif s == k:
                s += 1
            elif e == k:
                e -= 1
        elif A[s] + A[e] < target:
            s += 1
        else:
            e -= 1

print(rst)
