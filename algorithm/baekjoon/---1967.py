import sys,collections
input = sys.stdin.readline
q = collections.deque()

def BFS(v):
    q.append(1)
    visit[v] = 1
    while q:
        now = q.popleft()
        for new in tree[v]:
            if not visit[new[0]]:
                visit[new[0]] = visit[now[0]] + now[1]
                q.append(new[0])





n = int(input())
tree = [[] for _ in range(n+1)]
visit = [0] * (n+1)
for i in range(n-1):
    lst = list(map(int, input().split()))
    tree[lst[0]].append(lst[1:]) #[[자식,거리]]

print(tree)
BFS(1)
print(visit)