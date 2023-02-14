# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# lst = list(map(int, input().split()))
# S = [0] * N
# S[0] = lst[0]
#
# for i in range(1, N):
#     S[i] = S[i-1] + lst[i]
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     if a == 1:
#         print(S[b-1])
#     else:
#         print(S[b-1]-S[a-2])

#_-------------------

'''
prefix_sum = [0]
temp = 0
for i in numbers:
    temp += i
    prefix_sum.append(temp)

for i in range(M):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
'''