import sys
input = sys.stdin.readline

def is_prime(n):
    if n == 2:
        return True
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())

#몫이 1이 될때까지 반복
#나머지가 0이면서 소수인 수로 나누기 반복
