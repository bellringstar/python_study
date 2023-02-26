import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if A<B:
    A, B = B, A
def gcd(a,b): #a>b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print('1' * gcd(A,B))