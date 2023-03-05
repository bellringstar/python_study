'''
모든 건물을 짓는데 드는 최소 시간
건물 짓는데 순서가 존재 -> 노드의 순서? -> 위상정렬?
N개 건물에서 각 건물을 짓는데 드는 최소 시간 = output 최소 = 여러가지 중 최소
lst 길이가 2다 = 선수건물이 없다.
'''

import sys,collections
input = sys.stdin.readline

N = int(input()) #건물 개수
arr = [[] for _ in range(N+1)]
d = [0] * (N+1)
self = [0] * (N+1)

for i in range(1, N+1):
    lst = list(map(int, input().split()))
    self[i] = lst[0]
    idx = 1
    while True:
        tmp = lst[idx]
        idx += 1
        if tmp == -1:
            break
        arr[tmp].append((i))
        d[i] += 1

q = collections.deque()

rst = [0] *(N+1)

for i in range(1, N+1):
    if d[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for next in arr[now]:
        d[next] -= 1
        rst[next] = max(rst[next], rst[now] + self[now])
        if d[next] == 0:
            q.append(next)

for i in range(1, N+1):
    print(rst[i] + self[i])




