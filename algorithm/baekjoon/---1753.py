import sys,queue
input = sys.stdin.readline


V, E = map(int, input().split())

arr = [[] for _ in range(V+1)]
K = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))
visited = [0] * (V+1)
rst = [2000000] * (V+1)
rst[K] = 0

q = queue.PriorityQueue()
q.put((0, K))

while q.qsize()>0:
    now = q.get()
    if visited[now[1]]:
        continue
    visited[now[1]] = 1
    for new in arr[now[1]]:
        if rst[new[0]] > new[now[1]] + new[1]:
            rst[new[0]] = new[now[1]] + new[1]
            print(rst)
            q.put((rst[new[0]], new[1]))

for i in range(1, V+1):
    if visited[i]:
        print(rst[i])
    else:
        print("INF")
