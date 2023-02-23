import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(v):
    visit[v] = 1
    for w in tree[v]:
        if not visit[w]:
            lst[w] = v
            dfs(w)


N = int(input())
tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
visit = [0] * (N+1)
lst = [0] * (N+1)
dfs(1)
for i in range(2,len(lst)):
    print(lst[i])
