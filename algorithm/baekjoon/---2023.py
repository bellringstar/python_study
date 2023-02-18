'''
신기한 소수
ex)7331 -> 7 소수, 73 소수, 733 소수, 7331 소수
'''

import sys
input = sys.stdin.readline

N = int(input())
# prime = [True] * (10**N)
# prime[0] = prime[1] = False
# for i in range(2, (10**(N))):
#     if prime[i] == True:
#         for j in range(2*i, (10**(N)), i):
#             prime[j] = False
# _------메모리 초과
# def is_prime(num):
#     return prime[num]
def is_prime(num):
    import math
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
#--------시간초과

# def check(num, v=1):
#     global N
#     if not is_prime(num//v):
#         return False
#     if v == 10**(N-1):
#         return True
#     return check(num, v*10)
start = [2, 3, 5, 7]
A = [1, 3, 5, 7, 9]


def check(num):
    if len(str(num)) == N:
        return print(num)
    else:
        for i in A:
            if is_prime(num*10+i):
                check(num*10+i)

for i in start:
    check(i)