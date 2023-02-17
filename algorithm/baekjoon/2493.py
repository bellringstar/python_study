import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

stack = []
cnt = [0] * N

for i in range(N-1,-1,-1):
    while stack and arr[i] > arr[stack[-1]]:
        cnt[stack[-1]] = i + 1
        stack.pop()

    stack.append(i)

# while stack:
#     cnt[stack.pop()] = 0


print(*cnt)