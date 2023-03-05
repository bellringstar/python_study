#노드의 순서 -> 위상정렬
import collections,sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
D = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    D[b] += 1

q = collections.deque()
for idx in range(1, N+1):
    if D[idx] == 0:
        q.append(idx)

while q:
    now = q.popleft()
    print(now, end=' ')
    for num in arr[now]:
        D[num] -= 1
        if D[num] == 0:
            q.append(num)
