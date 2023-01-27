# import sys
# input = sys.stdin.readline

# def is_prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2, n):
#             if n%i == 0:
#                 return False
#     return True

# M, N = map(int, input().split())
# lst =[]
# for i in range(M, N+1):

#     if is_prime(i) and  :
#         print(i)

#------------------------------시간초과-----------------------------
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5 +1)):
        if n % i == 0:
            return False
    return True

import sys
input = sys.stdin.readline

M, N = map(int, input().split())

for i in range(M, N+1):
    if is_prime(i):
        print(i)


  


'''
91을 판정할때 2~90개를 다 계산한다?
'''