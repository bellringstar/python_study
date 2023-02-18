import collections

dq = collections.deque()

N = int(input())

for i in range(N,0,-1):
    dq.append(i)

for _ in range(N-1):
    dq.pop()
    dq.appendleft(dq.pop())

print(dq.pop())
