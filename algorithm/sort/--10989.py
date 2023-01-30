# 수 범위가 작다 -> 카운팅 정렬
# import sys

# input = sys.stdin.readline
# N = int(input())
# num_list = [0] * N
# for idx in range(N):
#     num_list[idx] = int(input())
# counting = [0] * (max(num_list) + 1)

# for num in num_list:
#     counting[num] += 1

# for i in range(1, len(counting)):
#     counting[i] += counting[i-1]

# rst = [0] * N

# for num in num_list:
#     rst[counting[num] - 1] = num
#     counting[num] -= 1

# for i in rst:
#     print(i)

#-------------메모리 초과----------------------
'''
1.count = [0] * (max(num_list)+1)
num_lust = [3,7,4,1,1]
count = [0, 2, 0, 1, 1, 0, 0, 1]
'''
# import sys
# input = sys.stdin.readline

# N = int(input())
# num_list = [0] * N
# for i in range(N):
#     num_list[i] = int(input())
# count = [0] * (max(num_list) + 1)

# for num in num_list:
#     count[num] += 1

# for idx in range(len(count)): #0,1,2,3,4,5,6,7
#     if count[idx] != 0: #idx = 1
#         for i in range(count[idx]):
#             print(idx)         
#-------------메모리초과-----------------------
