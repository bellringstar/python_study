N,M = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a%b

    return a

def LCM(a, b):
    return a * b // gcd(a, b)


print(gcd(N, M))
print(LCM(N, M))