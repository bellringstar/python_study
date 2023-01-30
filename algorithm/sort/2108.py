# import sys
# input = sys.stdin.readline

# N = int(input()) #홀수
# lst = []
# for _ in range(N):
#     lst.append(int(input()))

# def average(lst): #음수일때 처리 수정
#     avg = sum(lst) / len(lst)
#     # def round_up(n):
#     #     if int(n % 1 * 10) >= 5:
#     #         return int(n) + 1
#     #     else:
#     #         return int(n)
#     print(int(round(avg)))

# def median(lst):
#     lst.sort()
#     print(lst[len(lst)//2])

# def bound(lst):
#     print(lst[-1] - lst[0])

# def mod(lst): # [1,1,2,2,3,3,5] 최빈값 1,2,3 두번쨰로 작은 값 2
#     rst = []
#     for i in lst:
#         rst.append((i, lst.count(i)))
#     rst = list(set(rst))
#     rst.sort(key=lambda x:(-x[1],x[0]))
#     if len(rst)!=1 and rst[0][1] == rst[1][1]:
#         print(rst[1][0])
#     else:
#         print(rst[0][0])

# average(lst)
# median(lst)
# mod(lst)
# bound(lst)

#----------------------------------시간초과------------------
