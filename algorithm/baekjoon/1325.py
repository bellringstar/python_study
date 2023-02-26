# import sys, collections
# input = sys.stdin.readline
#
#
# def BFS(s):
#     q = collections.deque()
#     q.append(s)
#     v[s] = 1
#     while q:
#         now = q.popleft()
#         for new in arr[now]:
#             if not v[new]:
#                 v[new] = 1
#                 ans[new] += 1
#                 q.append(new)
#
#
#
# N,M = map(int, input().split())
# arr = [[] for _ in range(N+1)]
# for _ in range(M):
#     A, B = map(int, input().split())
#     arr[A].append(B)
#
# ans = [0] *(N+1)
# for i in range(1, N+1):
#     v = [0] * (N + 1)
#     BFS(i)
#
# maxV = 0
# for i in range(1, N+1):
#     maxV = max(maxV, ans[i])
#
# for idx in range(1, N+1):
#     if ans[idx] == maxV:
#         print(idx, end=' ')


import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
ans = [0] * (N+1)

def BFS(s):
    q = deque()
    q.append(s)
    v[s] = True
    while q:
        now = q.popleft()
        for new in arr[now]:
            if not v[new]:
                v[new] = True
                ans[new] += 1
                q.append(new)

for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)

for i in range(1, N+1):
    v = [False] * (N+1)
    BFS(i)

maxV = 0
for i in range(1, N+1):
    maxV = max(maxV, ans[i])

for i in range(1, N+1):
    if maxV == ans[i]:
        print(i, end=' ')