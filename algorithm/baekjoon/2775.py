# import sys
# input = sys.stdin.readline

# #a층의 b호에 살려면 자신의 아래(a-1)층의 1호 부터 b호까지 사람들의 수의 합
# #
# def floor_count(k, n):
#     sum_floor = 0
#     if k == 0:
#         return n
#     else:
#         for i in range(1, n+1):
#             sum_floor += floor_count(k-1, i)
#         return sum_floor
# T = int(input())
# for i in range(T):
#     k = int(input()) #k층 n호에는 몇명이 사는가
#     n = int(input())  # k = 1 n = 3 -> return 6/ k = 2, n = 3 ->10
#     #0층의 i호에는 i명이 산다 2층 3호 = 0층 1,2,3호 1층 1,2,3호 
#     #1층 1호 = 0층 1호, 1층 2호= 0층 1호, 2호, 1층 3호 = 0층 1,2,3호
#     print(floor_count(k, n))
#------------------------시간초과-------------------------------
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    room_list = list(range(1, n+1))
    for i in range(k):
        for j in range(2, n+1):
            room_list[j-1] += room_list[j-2]
    print(room_list[-1])

