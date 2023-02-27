import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n = int(input())
    phone = []
    for _ in range(n):
        phone.append(input().rstrip())
    print(phone)