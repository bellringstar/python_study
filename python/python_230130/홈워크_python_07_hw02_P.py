'''
1. 짝수라면 2로 나눈다.
2. 홀수라면 3을 곱하고 1을 더한다
3. 결과로 나온 수에 같은 작업을 1이 나올때까지 반복한다.
횟수를 리턴
'''
def collatz(n, count = 0):
    if n == 1:
        return count
    if count > 500:
        return -1
    if n % 2 : #홀수
        count += 1
        return collatz(n * 3 +1, count)
    else:
        count +=1
        return collatz(n//2, count)

# def collatz(n, count=0):
#     while n != 1:
#         if count > 500:
#             return -1
#         count += 1
#         if n % 2:   
#             n = n * 3 + 1
#         else:
#             n = n//2
#     return count

print(collatz(6))  # => 8
print(collatz(16))  # => 4
print(collatz(27))  # => 111
print(collatz(626331))  # => -1
