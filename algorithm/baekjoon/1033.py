import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N-1):
    a, b, p, q = map(int, input().split()) #a번 재료의 질량을 b번 재료의 질량으로 나눈 값이 p/q