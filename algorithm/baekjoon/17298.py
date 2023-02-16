'''
NGE(i) = 수열에서 Ai 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수
A = [9, 5, 4, 7, 8] NGE(1) = 없다. = -1/ NGE(2) : 7,8 = 7/ NGE(3): 7,8 = 7
기본적으로 마지막 NGE는 무조건 -1

'''
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = []
NGE = [0] * N

for i in range(N):
    while stack and (A[stack[-1]] < A[i]):
        idx = stack.pop()
        NGE[idx] = A[i]
    stack.append(i)



while stack:
    idx = stack.pop()
    NGE[idx] = -1

print(*NGE)


