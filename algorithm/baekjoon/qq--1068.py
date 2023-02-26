import sys
input = sys.stdin.readline

def dfs(s):
    global cnt
    visitied[s] = True
    for w in arr[s]:
        if not visitied[w]:
            dfs(w)
            if w not in p:
                cnt += 1

N = int(input())
p = list(map(int, input().split()))
node = int(input())

for i in range(N):
    if p[i] == -1:
        root = i
        break
arr = [[] for _ in range(N)]
for idx in range(N):
    if p[idx] == -1:
        continue
    arr[p[idx]].append(idx)


if node == root:
    print(0)
else:
    cnt = 0
    visitied = [False] * N
    visitied[node] = True
    dfs(root)
    print(cnt)
