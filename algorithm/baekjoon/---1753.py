import sys,collections

input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    arr[u].append((v,w))

# K에서 i까지 최단 경로
distance = [300000*100] * (V+1)
distance[K] = 0

def graph(s):
    q = collections.deque()
    q.append((s,0))
    while q:
        now = q.popleft()
        for new in arr[now[0]]:
            pos = new[0]
            v = new[1]
            distance[pos] = min(distance[pos], distance[now[0]] + v)
            q.append(new)
graph(K)
for i in range(1,V+1):
    if distance[i] == 300000*100:
        print("INF")
    else:
        print(distance[i])


