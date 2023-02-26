'''
1~N번의 도시, M개의 단방향 도로, 도로의 거리 1 => 가중치 없다.
X 도시로 부터 최단 거리가 K인 도시들의 번호 -> BFS // X->X : 거리 0
'''

def BFS(s):
    global K
    q = []
    q.append(s)
    v[s] = 1
    while q:
        now = q.pop(0)
        if v[now] == K+1:
            rst.append(now)
        if v[now] > K+1:
            return
        for new in lst[now]:
            if not v[new]:
                q.append(new)
                v[new] += v[now] + 1


import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split()) #N:도시개수, M:도로 개수, K:거리정보, X: 출발점
lst = [[] for _ in range(N+1)] #1부터 시작
for _ in range(M):
    A, B = map(int, input().split())
    lst[A].append(B)

v = [0] * (N+1)
rst = []
BFS(X)
rst.sort()
if rst:
    for num in rst:
        print(num)
else:
    print(-1)

