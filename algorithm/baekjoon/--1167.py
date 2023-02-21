import sys, collections
input = sys.stdin.readline
queue = collections.deque()

V = int(input())
arr = [[] for _ in range(V+1)]

for i in range(V):
    node = list(map(int, input().split()))
    arr[node[0]] = tuple(node[1:-1])

def BFS(v):
    queue.append(v)
    visited[v] = 1
    while queue:
        now = queue.popleft() #1
        for j in range(0,len(arr[now]),2):
            if not visited[arr[now][j]]:
                queue.append(arr[now][j])
                visited[arr[now][j]] = visited[now] + arr[now][j+1]




# ans = 0
# for i in range(1, V+1):
#     visited = [0] * (V + 1)
#     BFS(i)
#     ans = max(ans, max(visited))
#
# print(ans-1)   시간초과

#임의의 노드에서 가장 긴 경로로 연결돼 있는 노드는 트리의 지름에 해당하는 두 노드 중 하나다.

visited = [0] * (V + 1)
BFS(1)
Max = 1
for i in range(2, V+1):
    if visited[Max] < visited[i]:
        Max = i #거리 중 최대값


visited = [0] * (V + 1)
BFS(Max)
print(max(visited) - 1)
