import sys,heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,w = map(int, input().split())
    arr[s].append((w,e))

start, end = map(int, input().split())

cost = [float("INF")] * (N+1)
cost[start] = 0
q = []
heapq.heappush(q, (0,start))
visited = [False] * (N+1)
while q:
    now = heapq.heappop(q)
    pos = now[1]
    w = now[0]
    if pos == end:
        print(cost[end])
        break
    if visited[pos]:
        continue
    visited[pos] = True
    for new in arr[pos]:
        if cost[new[1]] > cost[pos] + new[0]:
            cost[new[1]] = cost[pos] + new[0]
            heapq.heappush(q,(cost[new[1]],new[1]))


