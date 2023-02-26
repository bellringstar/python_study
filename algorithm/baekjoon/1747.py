import sys, math
input = sys.stdin.readline

N = int(input())

prime = [1] * (10**7)
prime[0] = prime[1] = 0

for i in range(2, int(math.sqrt(10**7))):
    if prime[i] == 0:
        continue
    for j in range(i+i, 10**7, i):
        prime[j] = 0

def palindrome(num):
    length = len(num)
    for i in range(length//2):
        if num[i] == num[-i-1]:
            continue
        else:
            return False
    return True

for num in range(N, 10**7):
    if prime[num] and palindrome(str(num)):
        print(num)
        break


