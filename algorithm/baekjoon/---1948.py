'''
도로가 일방통행 -> 빙행 그래프
사이클이 없다.
무수히 많은 사람 시작노드 -> 도착노드 가능한 모든 경로
도착 도시에서 모두 다시 만난다.
출발 후 최소 몇 시간 후에 모두 만나는가? -> 가장 늦은 사람 기준으로 만나게 된다.
그리고 가장 늦은 사람은 쉬지 않고 달려야한다. 이런 사람들이 지나는 도로의 수를 카운트


'''

# import sys
# input = sys.stdin.readline
# 
# def DFSBFS(s,e):
#     global cnt, time
#     stack.append(s)
#     now = stack.pop()
#     visited[now[0]] = 1
#     arr.append(now)
#     for new in path[now[0]]:
#         if not visited[new[0]]:
#             DFSBFS(new,e)
#             visited[new[0]] = 0
#             if new[0] == e:
#                 sum = 0
#                 for route in arr:
#                     sum += route[1]
#                 if time <= sum:
#                     time = sum
#                 cnt = max(cnt,len(arr))
#             arr.pop()
# 
# 
# n = int(input())
# m = int(input())
# path = [[] for _ in range(n+1)]
# for _ in range(m):
#     s, e, t = map(int, input().split())
#     path[s].append((e,t)) #s에서 e로 t시간 걸린다 인접리스트
# 
# d = [0] * (n+1)
# for idx in range(1, n+1):
#     for r in path[idx]:
#         d[r[0]] += 1
# 
# s_city, e_city = map(int, input().split()) #시작도시, 도착도시
# 
# 
# stack = []
# 
# visited = [0] * (n+1)
# arr = []
# cnt = time = 0
# DFSBFS((s_city,0),e_city)
# print(time)
# print(cnt)
#------------------------------시간초과