'''
임의의 자연수 n에 대하여 n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재
'''

# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n**0.5 +1)):
#         if n % i == 0:
#             return False
#     return True


# while True:
#     n = int(input())
#     cnt = 0
#     if n == 0:
#         break
#     for i in range(n+1, 2*n+1):
#         if is_prime(i):
#             cnt+=1
#     print(cnt)
#====================================시간초과------------------
# import sys
# input = sys.stdin.readline

# while True:
#     n = int(input())
#     cnt = 0
#     if n == 0:
#         break
#     prime = [True] * (2*n + 1)
#     for x in range(2, 2*n+1):
#         if prime[x] == True:
#             for y in range(2*x, 2*n+1, x):
#                 prime[y] = False
#     prime[0] = False; prime[1] = False
#     for i in prime[n+1:]:
#         if i == True:
#             cnt +=1
#     print(cnt)
#--------------------------------------오래걸림----------------

    
