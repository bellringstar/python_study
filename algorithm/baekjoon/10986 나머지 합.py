'''
N개의 수 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수
'''

# import sys
# input = sys.stdin.readline
#
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# S = [0] * N
#
# rst = 0
# for num in arr:
#     if num % M == 0:
#         rst += 1
#
#
# k = 1
# while k<N:
#     for i in range(k):
#         S[i] = arr[i]
#     for i in range(k, N):
#         S[i] = S[i-1] + arr[i]
#
#     for j in range(k, N):
#         if S[j] % M == 0:
#             rst += 1
#     k += 1
# print(rst)
# 시간초과


# import sys
# input = sys.stdin.readline
#
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# S = [arr[0]] * N
#
# rst = 0
# for i in range(1, N):
#     S[i] = S[i-1] + arr[i]
#
# for i in range(N):
#     S[i] = S[i] % M
#     if S[i] == 0:
#         rst += 1
#
# dic_count = {key: S.count(key) for key in S} -> N^2 걸림 S를 N개 순회, 하나마다 count로 전부 순회
# for i in dic_count.keys():
#     rst += (dic_count[i] * (dic_count[i] - 1) // 2)
#
# print(rst)

#-----------------------시간초과

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
S = [arr[0]] * N
C = [0] * M

rst = 0
for i in range(1, N):
    S[i] = S[i-1] + arr[i]

for i in range(N):
    r = S[i] % M
    if r == 0:
        rst += 1
    C[r] += 1


for i in range(M):
    if C[i] > 1:
        rst += (C[i] * (C[i] - 1) // 2)

print(rst)