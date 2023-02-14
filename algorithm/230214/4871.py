# class Node:
#     def __init__(self, item, next):
#         self.item = item
#         self.next = next
#
# class Stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, item):
#         self.head = Node(item, self.head)
#
#     def pop(self):
#         if self.head == None:
#             return -1
#         item = self.head.item
#         self.head = self.head.next
#         return item
#
#     def top(self):
#         return self.head.item

# def dfs(v, target):
#     s = Stack()
#     s.push(v)
#     visited[v] = 1
#     while s.head != None:
#         for w, val in enumerate(arr[v]):
#             if val == 1 and visited[w] == 0:
#                 s.push(v)
#                 if w == target:
#                     return 1
#                 v = w
#                 visited[v] = 1
#                 break
#         else:
#             v = s.pop()
#     return 0

'''
v = 시작점 방문처리/ 스택에 쌓기
v에서 갈 수 있는 점(방문x한 점) w 할당
v = w
방문처리/ 스택에 쌓기

갈수있는 점이 없다.
v = stack.pop()
다시 갈수있는 점 있나 체크
있다 -> v를 스택에 push하고 w 찾아 할당
없다 -> 다시 pop
v가 스택에 있고, target이 스택에 있다 = 정답
'''



# def dfs(v, target):
#     stack = [v]
#     visited[v] = 1
#     while stack:
#         if stack[-1] == target:
#             return 1
#         for w, val in enumerate(arr[v]):
#             if val == 1 and visited[w] == 0:
#                 visited[w] = 1
#                 v = w
#                 stack.append(v)
#                 break
#         else:
#             stack.pop()
#             if stack:
#                 v = stack[-1]
#     return 0
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     rst = 0
#     V, E = map(int, input().split())
#     arr = [[0] *(V+1) for _ in range(V+1)]
#     for _ in range(E):
#         x, y = map(int, input().split())
#         arr[x][y] = 1
#         arr[y][x] = 1
#     S, G = map(int, input().split())
#     visited = [0] * (V+1)
#     rst = dfs(S, G)
#     print(f'#{tc} {rst}')


# def dfs(v, target):
#     stack = []
#     stack.append(v)
#
#     while stack:
#         v = stack.pop()
#         if visited[v] == 0:
#             visited[v] = 1
#
#             for w in range(1, V+1):
#                 if arr[v][w] == 1 and visited[w] == 0:
#                     if w == target:
#                         return 1
#                     stack.append(w)
#     return 0
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#
#     V, E = map(int,input().split())
#     arr = [[0] *(V+1) for _ in range(V+1)]
#
#     for _ in range(E):
#         x, y = map(int,input().split())
#         arr[x][y] = 1
#
#     S, G = map(int,input().split())
#     visited = [0 for _ in range(V + 1)]
#     rst = dfs(S, G)
#     print(f'#{tc} {rst}')


def dfs(v, target):
    stack = [v]
    visited = [0] * (V+1)

    while stack:
        if stack[-1] == target:
            return 1
        visited[v] = 1
        for w in range(V+1):
            if not visited[w]:
                if arr[v][w]:
                    stack.append(w)
                    v = w
                    break
        else:
            stack.pop()
            if stack:
                v = stack[-1]
    else:
        return 0

T = int(input())
for tc in range(1, T+1):

    V, E = map(int,input().split())
    arr = [[0] *(V+1) for _ in range(V+1)]

    for _ in range(E):
        x, y = map(int,input().split())
        arr[x][y] = 1

    S, G = map(int,input().split())
    rst = dfs(S, G)
    print(f'#{tc} {rst}')
