# import sys
# input = sys.stdin.readline
#
#
# def dfs(v):
#     global cnt
#     visited[v] = True
#     for w in arr[v]:
#         if not visited[w]:
#             dfs(w)
#             cnt += 1
#
#
# N = int(input())
# p = list(map(int, input().split()))
# node = int(input())
#
# arr = [[] for _ in range(N)]
# for idx in range(N):
#     if p[idx] != -1:
#         arr[p[idx]].append(idx)
# print(arr) #[[1, 2], [], [3, 4], [], [5, 6], [], [7, 8], [], []]

# q = []
# q.append(node)
# while q:
#     now = q.pop(0)
#     while arr[now]:
#         q.append(arr[now].pop(0))
#     arr[now] = -1
#
# cnt = 0
#
# for row in arr:
#     if not row:
#         cnt += 1
#
# print(cnt)
import sys
input = sys.stdin.readline


def dfs(v):
    global cnt
    visited[v] = True
    for w in arr[v]:
        if not visited[w]:
            dfs(w)
            if w not in p:
                cnt += 1


N = int(input())
p = list(map(int, input().split()))
node = int(input())
cnt = 0
arr = [[] for _ in range(N)]
for idx in range(N):
    if p[idx] != -1:
        arr[p[idx]].append(idx)

visited = [False] * N
visited[node] = True
for idx in range(N):
    if p[idx] == -1:
        v = idx
        break

if node == v:
    print(0)
else:
    dfs(v)
    print(cnt)


