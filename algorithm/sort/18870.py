# import time
# import sys
# start = time.time()
# input = sys.stdin.readline

# N = int(input())
# lst = list(map(int, input().split()))
# '''
# 해당 수 보다 작은것의 개수 [2, 4, -10, 4, -9]
# 2보다 작은것의 개수 -10, -9 = 2개
# 4보다 작은것의 개수 2, -10, -9 3개
# ....
# 작은것 판정 
# 1. 자신을 제외한 나머지와 전부 비교
# 2. 이미 한번 비교 한 놈은 패스
# '''
# rst = []
# for idx in range(N):
#     cnt = 0
#     stack = [] 
#     for num in lst:
#         if  num not in stack and lst[idx] > num:
#             cnt +=1
#             stack.append(num)
#     rst.append(cnt)
# print(rst)
# print(time.time()- start)
#------------------시간초과---------------------
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
new_list = list(set(lst))
new_list.sort()
dic = {new_list[idx]:idx for idx in range(len(new_list))}
for num in lst:
    print(dic[num],end=" ")
