'''
BFS
'''
import sys,collections
q = collections.deque()


def bfs(s):
    q.append(s)
    visit[s][1] = 1
    while q:
        now = q.popleft()
        for new in arr[now]:
            if not visit[new][1]:
                visit[new][1] = visit[now][1] + 1
                q.append(new)

for tc in range(1, 11):
    N, s = map(int,input().split())
    lst = list(map(int,input().split()))
    size = max(lst)
    arr = [[] for _ in range(size + 1)]
    visit = [[idx,0] for idx in range(size+1)]

    for i in range(0, N, 2):
        arr[lst[i]].append(lst[i+1])

    bfs(s)
    visit.sort(key=lambda x:(x[1],x[0]),reverse=True)
    print(f'#{tc} {visit[0][0]}')