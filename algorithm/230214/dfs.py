V = 7+1 #(0번은 안쓸거임)
# G = [[0,0,0,0,0,0,0,0],
#     [0,0,1,1,0,0,0,0],
#     [0,1,0,0,1,1,0,0],
#     [0,1,0,0,0,0,0,1],
#     [0,0,1,0,0,0,1,0],
#     [0,0,1,0,0,0,1,0],
#     [0,0,0,0,0,1,0,1],
#     [0,0,0,1,0,0,0,1]]

# G = [[0]*V for _ in range(V)]
# # print(G)
# for idx in range(0, len(S), 2):
#     v1 = S[idx]
#     v2 = S[idx+1]
#     G[v1][v2] = 1
#     G[v2][v1] = 1
# print(G)


# G = [[] for _ in range(V)]
# print(S, G)

# for idx in range(0, len(S), 2):
#     v1 = S[idx]
#     v2 = S[idx+1]
#     G[v1].append(v2)
#     G[v2].append(v1)

G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]

visited = [False] * V
def dfsr(v):
    print(v)
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            dfsr(w)
dfsr(1)

def dfs(v):
    ST = []
    visited = [False] * V

    ST.append(v)
    visited[v] = True
    while ST:
        v = ST.pop()
        print(v)
        for w in G[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = True

# def dfs(v):
#     ST = []
#     visited = [False] * V
#
#     ST.append(v)
#     while ST:
#         v = ST.pop()
#         if not visited[v]:
#             visited[v] = True
#             print(v)
#
#         for w in G[v]:
#             if not visited[w]:
#                 ST.append(w)



# def dfs(v):
#     ST = []
#     visited = [False] * V
#
#     ST.append(v)
#     visited[v] = True
#     print(v)
#     while ST:   #len(ST) > 0:
#         for w in G[v]:
#             if not visited[w]:
#                 visited[w] = True
#                 print(w)
#                 ST.append(v)
#                 v = w
#                 break
#         else:
#             v = ST.pop()

# dfs(1)





