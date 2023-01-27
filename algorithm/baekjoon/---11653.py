# import sys
# input = sys.stdin.readline

# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n**0.5 +1)):
#         if n % i == 0:
#             return False
#     return True

# N = int(input())
# i = 2
# while N != 1:
#     if is_prime(i) and N % i == 0:
#         N = N//i
#         print(i)
#     else:
#         i += 1    

#--------------------------시간초과-------------------------

#1. prime 판정 변화