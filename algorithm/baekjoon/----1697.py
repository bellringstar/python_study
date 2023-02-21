import sys, collections
input = sys.stdin.readline
queue = collections.deque()

N, K = map(int, input().split())
queue.append(N)
v_dic = {N:0}

while queue:
    now = queue.popleft()
    if now == K:
        print(v_dic[K])
        exit(0)
    for new in (now-1, now+1, now*2):
        if new not in v_dic.keys() and 0<=new<=K:
            v_dic[new] = v_dic[now] + 1
            queue.append(new)
    print(v_dic)


from collections import deque

def BFS():
    queue = deque()
    queue.append(N)
    while queue:
        now = queue.popleft()
        if now == K:
            print(visited[now])
            return
        for new in (now+1, now-1, now*2):
            if 0 <= new <= MAX and not visited[new]:
                visited[new] = visited[now] + 1
                queue.append(new)

MAX = 10 ** 5
visited = [0] * (MAX + 1)
N, K = map(int, input().split())
BFS()
