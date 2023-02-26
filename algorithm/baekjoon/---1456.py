import sys,math
input = sys.stdin.readline

A, B = map(int, input().split())

prime = [1] * (10**7 + 1)
prime[0] = prime[1] = 0
length = len(prime)

for i in range(2, int(math.sqrt(length) + 1)):
    if prime[i] == 0:
        continue
    for j in range(i+i, length, i): #i의 배수 전부 0처리
        prime[j] = 0

# def is_prime(num):
#     if num == 0 or num == 1:
#         return False
#     if num == 2:
#         return True
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True

cnt = 0
for idx in range(2, 10**7+1):
    k = 2
    if prime[idx] == 1:
        start_num = idx
        num = start_num ** k
        while num <= B:
            if num >= A:
                cnt += 1
            k += 1
            num = start_num ** k

print(cnt)


