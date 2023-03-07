'''
k번째 최단 경로 -> 거리를 계속해서 추가 후 정렬
'''
import sys,heapq
input = sys.stdin.readline
n, m, k = map(int, input().split())

arr = [[] for _ in range(n+1)]
distance = [[0] for _ in range(n+1)]
q = [(0,1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((c,b)) #c시간, b 목적지

while q:
    now = heapq.heappop(q)
    pos = now[1]
    weight = now[0]
    route = []
    for new in arr[pos]:
        new_pos = new[1]
        new_weight = new[0]
        heapq.heappush(distance[new_pos],distance[pos][0] + new_weight)
        print(distance)
        heapq.heappush(q, (distance[pos][0] + weight, new_pos))
